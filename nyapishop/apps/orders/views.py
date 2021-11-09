from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .models import *
from products.models import ProductImage, Product,Mailig
from .forms import *
from django.contrib.auth.models import User
from shop.models import Profile
from django.contrib.auth.views import LoginView

def basket_adding(request):
    return_dict ={}
    session_key = request.session.session_key
    # print('this basket_adding:')
    # print('request.POST:',request.POST)
    data = request.POST
    # print('data:',data)
    product_id = data.get("product_id")
    count = data.get("count")
    img_number = ProductImage.objects.get(product__id=product_id,is_main_image = 1)
    # catalog = Product.objects.get(id=product_id).product_catalog
    # print(type(img_number))
    new_product, created = ProductInBasket.objects.get_or_create(session_key = session_key , product_id  =product_id ,images=img_number,
                                                                 defaults={"count": count})

    if not created:
        new_product.count += int(count)
        new_product.save(force_update = True)

    products_total_count = ProductInBasket.objects.filter(session_key = session_key).count()
    return_dict["products_total_count"] = products_total_count

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key = session_key)

    # print(products_in_basket)
    # product_images = ProductImage.objects.filter(is_main_image=1)
    # imgs = []
    # for value in products_in_basket:
    #     imgs.append(value.product.id)
    #
    # print(imgs)
    mail_form = MailingFormsOrder(request.POST or None)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)

        if request.POST.get('is_delete'):
            product_id = request.POST.get('product_id')
            print("Delete this element")
            product = ProductInBasket.objects.filter( id  =product_id)
            print(product)

            product.delete()
            return_dict = {}
            products_total_count = ProductInBasket.objects.filter(session_key = session_key).count()
            return_dict["products_total_count"] = products_total_count

            return JsonResponse(return_dict)
        elif request.POST.get('is_delete_all'):
            products = ProductInBasket.objects.filter(session_key = session_key)
            print(products)
            products.delete()
            return_dict = {}
            products_total_count = ProductInBasket.objects.filter(session_key=session_key).count()
            return_dict["products_total_count"] = products_total_count

            return JsonResponse(return_dict)
        elif request.POST.get('emaill'):
            Mailig.objects.create(email=request.POST.get("emaill"))
        elif request.POST.get('snp'):
            data = request.POST
            print(data)
            user_this = request.user
            dost=[]
            dost1 = []
            print('------')

            first  = str(str(str(data).split('adress')[-1]).split('snp')[0]).replace(',','').replace('\'','').replace(']','').replace(":",'').replace('[','')
                # replace('adress','').replace(":",'').replace('[','').replace('\'','').replace(']','').split(',')
            print(first)

            print('------')
            # for item in dost:
            #     if item != " ":
            #         dost1.append(item)

            dostavka = first
            print(dostavka)

            phone = data["phone"]
            name = data["snp"]
            username = name
            email = data["email"]
            # dostavka = data["date"]
            other = data["other"]
            user, created = User.objects.get_or_create(username=phone,defaults={"first_name": name,})
            profile = Profile.objects.get(user=user)
            order = Order.objects.create(user=user, customer_snp=name, customer_email=email, customer_phone=phone,
                                         customer_other_information=other, customer_dostavka=dostavka,profile=profile)
            Profile.objects.filter(user=user).update(name=name, phone=phone)

            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    id_product_in_basket = name.split("product_in_basket_")[-1]
                    product_in_basket = ProductInBasket.objects.get(id=id_product_in_basket)
                    product_in_basket.count = int(value)
                    product_in_basket.save()
                    ProductInOrder.objects.create(product=product_in_basket.product, count=product_in_basket.count,
                                                  total_price=product_in_basket.total_price,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  order=order)
            # return redirect("http://127.0.0.1:8000/eto_uspeh",locals())

            return render(request, 'shop/uspeh.html', locals())

        else:
            print('no')
    return render(request, 'orders/checkout.html', locals())
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import FilterForm
from django.contrib.auth import authenticate, login, logout
from products.forms import Mailing
from products.models import ProductImage, Product, Mailig, Categories
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib.auth.models import User


# from .forms import  UserRegistrationForm


def main(request):
    paginate = ProductImage.objects.filter(is_main_image=1).count() / 20
    count_pag = int(paginate) + 1
    next_page = 2
    mail_form = MailingForms()
    if request.method == "POST":
        if "emaill" in request.POST:
            Mailig.objects.create(email=request.POST.get("emaill"))
        # print("POST",request.POST)
        # form_mailing = MailingForm(request.POST or None)
        # print(request)

        # if form.is_valid():
        #     print("FORM VALID")
        #     form.save()
        # print(form)
        # print(form.cleaned_data.get('email'))
        # Mailing.objects.create(email=form.cleaned_data.get('email'))

    # else:
    # form = MailingForm()
    # print("NONONONO")
    # if request.method == "GET":
    # print("asdasdasdasdas")
    # print(request.method('get'))
    query = request.GET.get('q')
    sorted = request.GET.get('ordering')
    # products = Product.objects.all()
    from_sorted = FilterForm(request.GET)
    print(request.POST)
    if query:
        # print(query)
        products_images = ProductImage.objects.filter(is_main_image=1, product__product_title__contains=query)[0:20]
    elif sorted:

        print("from_sorted", request.GET)
        if from_sorted.is_valid():
            data = from_sorted.cleaned_data["ordering"]
            print('data', data)
            if data == 'product_price_min':
                products_images = ProductImage.objects.filter(is_main_image=1).order_by(
                    'product__product_price').reverse()[0:20]
            if data == 'product_price_max':
                products_images = ProductImage.objects.filter(is_main_image=1).order_by('product__product_price')[0:20]
            if data == 'product_title_min':
                products_images = ProductImage.objects.filter(is_main_image=1).order_by('product__product_title')[0:20]
            if data == 'product_title_max':
                products_images = ProductImage.objects.filter(is_main_image=1).order_by(
                    'product__product_title').reverse()[
                                  0:20]
            if data == 'no_ordering':
                products_images = ProductImage.objects.filter(is_main_image=1)[0:20]
            # if from_sorted.cleaned_data["ordering"]:
            #     products_images =ProductImage.objects.order_by("product__"+from_sorted.cleaned_data["ordering"])[0:20]
            # if from_sorted.cleaned_data["product_price"]:
            #     products_images = ProductImage.objects.order_by("product__" + from_sorted.cleaned_data["product_price"])[
            #                       0:20]

    else:
        products_images = ProductImage.objects.filter(is_main_image=1)[0:20]

    return render(request, 'shop/main.html', locals())


def main_with_page(request, main_page):
    first_index = (main_page - 1) * 20
    last_index = main_page * 20
    products_images = ProductImage.objects.filter(is_main_image=1)[first_index:last_index]
    paginate = ProductImage.objects.filter(is_main_image=1).count() / 20
    count_pag = int(paginate) + 1
    prev_page = main_page - 1
    if main_page != count_pag:
        next_page = main_page + 1
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/main.html', locals())


def catalog_first(request, id_category):
    catalogs = Categories.objects.get(id=id_category)
    lists_catalogs = list(Categories.objects.all())
    catalog = [x.category for x in lists_catalogs]
    childs = Categories.objects.filter(id_parent=id_category)
    child_list = []
    child_parent_list = []
    print(childs)
    for child in childs:
        child_list.append(str(child))
    for item in child_list:
        child_parent_list.append(item.split(' -> ')[-1])
    parent_keys = []
    parent_value = []
    for value in child_parent_list:
        if value in catalog:
            parent_value.append(value)
            parent_keys.append(Categories.objects.get(category=value).id)
    print(parent_value)
    parrent_zip = zip(parent_keys, parent_value)
    parent = catalogs.id_parent
    catalog_string = str(catalogs).split(' -> ')
    lst = []
    for value in catalog_string:
        if value in catalog:
            lst.append(Categories.objects.get(category=value).id)
    # print(catalog_string)
    asd = zip(catalog_string[:-1], lst[:-1])
    catalog_name = catalog_string[-1]

    price_form = PriceFilterForm(request.GET)
    # print(price_form)
    print(request)
    # search = request.GET.get('search')
    from_sorted = FilterForm(request.GET)
    price_left = request.GET.get('price_left')
    price_rigft = request.GET.get('price_right')
    sorted = request.GET.get('ordering')
    if price_left or price_rigft:
        print('search')
        if price_left:
            products_images = ProductImage.objects.filter(is_main_image=1,
                                                          product__product_tree_catalog__contains=catalog_string[-1],
                                                          product__product_price__gte=request.GET.get('price_left'))[
                              0:20]
        if price_rigft:
            products_images = ProductImage.objects.filter(is_main_image=1,
                                                          product__product_tree_catalog__contains=catalog_string[-1],
                                                          product__product_price__lte=request.GET.get('price_right'))[
                              0:20]
    else:
        products_images = ProductImage.objects.filter(is_main_image=1,
                                                      product__product_tree_catalog__contains=catalog_string[-1])[0:20]

    if sorted:

        print("from_sorted", request.GET)
        if from_sorted.is_valid():
            data = from_sorted.cleaned_data["ordering"]
            print('data', data)
            if data == 'product_price_min':
                products_images = ProductImage.objects.filter(is_main_image=1,
                                                              product__product_tree_catalog__contains=catalog_string[
                                                                  -1]).order_by('product__product_price').reverse()[
                                  0:20]
            if data == 'product_price_max':
                products_images = ProductImage.objects.filter(is_main_image=1,
                                                              product__product_tree_catalog__contains=catalog_string[
                                                                  -1]).order_by('product__product_price')[0:20]
            if data == 'product_title_min':
                products_images = ProductImage.objects.filter(is_main_image=1,
                                                              product__product_tree_catalog__contains=catalog_string[
                                                                  -1]).order_by('product__product_title')[0:20]
            if data == 'product_title_max':
                products_images = ProductImage.objects.filter(is_main_image=1,
                                                              product__product_tree_catalog__contains=catalog_string[
                                                                  -1]).order_by('product__product_title').reverse()[
                                  0:20]
            if data == 'no_ordering':
                products_images = ProductImage.objects.filter(is_main_image=1,
                                                              product__product_tree_catalog__contains=catalog_string[
                                                                  -1])[0:20]

    paginate = ProductImage.objects.filter(is_main_image=1,
                                           product__product_tree_catalog__contains=catalog_string[-1]).count() / 20
    count_pag = int(paginate) + 1
    next_page = 2
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))

    return render(request, 'shop/catalog.html', locals())


#
#
# def first_catalog_first(request, first_catalog_name):
#     product_catalog = Product.objects.filter(fifth=first_catalog_name)
#     products_images = ProductImage.objects.filter(is_main_image=1, product__fifth=first_catalog_name)[0:20]
#
#     return render(request, 'shop/catalog.html', locals())
#
# def second_catalog_first(request, second_catalog_name):
#     product_catalog = Product.objects.filter(fourth=second_catalog_name)
#     products_images = ProductImage.objects.filter(is_main_image=1, product__fourth=second_catalog_name)[0:20]
#
#     return render(request, 'shop/catalog.html', locals())
#
def catalog_with_page(request, id_category, catalog_page):
    price_form = PriceFilterForm(request.GET)
    first_index = (catalog_page - 1) * 20
    last_index = catalog_page * 20

    catalogs = Categories.objects.get(id=id_category)
    lists_catalogs = list(Categories.objects.all())
    catalog = [x.category for x in lists_catalogs]
    childs = Categories.objects.filter(id_parent=id_category)
    child_list = []
    child_parent_list = []
    for child in childs:
        child_list.append(str(child))
    for item in child_list:
        child_parent_list.append(item.split(' -> ')[-1])
    parent_keys = []
    parent_value = []
    for value in child_parent_list:
        if value in catalog:
            parent_value.append(value)
            parent_keys.append(Categories.objects.get(category=value).id)
    parrent_zip = zip(parent_keys, parent_value)
    parent = catalogs.id_parent
    catalog_string = str(catalogs).split(' -> ')
    lst = []
    for value in catalog_string:
        if value in catalog:
            lst.append(Categories.objects.get(category=value).id)
    asd = zip(catalog_string[:-1], lst[:-1])
    catalog_name = catalog_string[-1]
    products_images = ProductImage.objects.filter(is_main_image=1,
                                                  product__product_tree_catalog__contains=catalog_string[-1])[
                      first_index:last_index]

    first_index = (catalog_page - 1) * 20
    last_index = catalog_page * 20
    paginate = ProductImage.objects.filter(is_main_image=1,
                                           product__product_tree_catalog__contains=catalog_string[-1]).count() / 20
    count_pag = int(paginate) + 1
    prev_page = catalog_page - 1
    if catalog_page != count_pag:
        next_page = catalog_page + 1
    mail_form = MailingForms()
    from_sorted = FilterForm(request.GET)
    price_left = request.GET.get('price_left')
    price_rigft = request.GET.get('price_right')
    sorted = request.GET.get('ordering')
    if price_left or price_rigft:
        print('search')
        if price_left:
            products_images = ProductImage.objects.filter(is_main_image=1,
                                                          product__product_tree_catalog__contains=catalog_string[-1],
                                                          product__product_price__gte=request.GET.get('price_left'))[
                              first_index:last_index]
        if price_rigft:
            products_images = ProductImage.objects.filter(is_main_image=1,
                                                          product__product_tree_catalog__contains=catalog_string[-1],
                                                          product__product_price__lte=request.GET.get('price_right'))[
                              first_index:last_index]
    else:
        products_images = ProductImage.objects.filter(is_main_image=1,
                                                      product__product_tree_catalog__contains=catalog_string[-1])[
                          first_index:last_index]

    if sorted:

        print("from_sorted", request.GET)
        if from_sorted.is_valid():
            data = from_sorted.cleaned_data["ordering"]
            print('data', data)
            if data == 'product_price_min':
                products_images = ProductImage.objects.filter(is_main_image=1,
                                                              product__product_tree_catalog__contains=catalog_string[
                                                                  -1]).order_by('product__product_price').reverse()[
                                  first_index:last_index]
            if data == 'product_price_max':
                products_images = ProductImage.objects.filter(is_main_image=1,
                                                              product__product_tree_catalog__contains=catalog_string[
                                                                  -1]).order_by('product__product_price')[
                                  first_index:last_index]
            if data == 'product_title_min':
                products_images = ProductImage.objects.filter(is_main_image=1,
                                                              product__product_tree_catalog__contains=catalog_string[
                                                                  -1]).order_by('product__product_title')[
                                  first_index:last_index]
            if data == 'product_title_max':
                products_images = ProductImage.objects.filter(is_main_image=1,
                                                              product__product_tree_catalog__contains=catalog_string[
                                                                  -1]).order_by('product__product_title').reverse()[
                                  0:20]
            if data == 'no_ordering':
                products_images = ProductImage.objects.filter(is_main_image=1,
                                                              product__product_tree_catalog__contains=catalog_string[
                                                                  -1])[first_index:last_index]
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))

    return render(request, 'shop/catalog.html', locals())


def registred(request):
    if request.method == 'POST':
        print(request.POST)

        form = SignUpForm(request.POST)
        if 'sirname' in request.POST:
            if form.is_valid():
                user = form.save()
                # user.email=form.cleaned_data.get('username')
                username = form.cleaned_data.get('username')
                name = form.cleaned_data.get('name')
                sirname = form.cleaned_data.get('sirname')
                secname = form.cleaned_data.get('secname')
                phone = form.cleaned_data.get('phone')
                comment = form.cleaned_data.get('comment')
                country = form.cleaned_data.get('country')
                profile = Profile.objects.filter(user_id=user.id)
                profile.update(name=name, sirname=sirname, secname=secname, comment=comment, country=country
                               , phone=phone)
                User.objects.filter(id=user.id).update(email=username)
                # User.objects.create(email = username)
                # user.save()
                print('ok')
                return render(request, 'shop/main.html', locals())
    else:
        form = SignUpForm()
        return render(request, 'shop/registred.html', {'form': form})
    return render(request, 'shop/registred.html', locals())


def user_agreement(request):
    return render(request, 'shop/user_agreement.html')


def auth(request):
    formauth = AuthUserForm(request.POST or None)
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        # if user is not None:
        login(request, user)
        # if formauth.is_valid():
        #     print("asdasdasdasdasasdasdasdaasdasdasdasdasd")
        #     formauth.save()
        #     return render(request, 'shop/main.html', locals())
        # else:
        # form = MailingForms(request.POST)

    # else:
    # formauth = AuthUserForm()
    return render(request, 'shop/auth.html', locals())


def password_forgot(request):
    if request.method == "POST":
        PasswordForgot.objects.create(email=request.POST.get('email_password_forgot'))
    #     if formpass.is_valid():
    #         formpass.save()
    #         return render(request, 'shop/main.html', locals())
    # else:
    # form = MailingForms(request.POST)

    # else:
    #     formpass = PasswordForgot()
    return render(request, 'shop/password_forgot.html', locals())


def user_info(request):
    user = request.user
    user_info = Profile.objects.get(user=user)
    if request.method == "POST":
        if request.POST.get('logout'):
            user = User.objects.get(username=request.POST.get('user_logout'))
            logout(request)

    return render(request, 'shop/user_info.html', locals())


def user_info_setting(request):
    user = request.user
    user_info = Profile.objects.get(user=user)
    print(request.POST)
    if request.method == "POST":
        if request.POST.get('logout'):
            user = User.objects.get(username=request.POST.get('user_logout'))
            logout(request)
        else:
            Profile.objects.update(name=request.POST.get('user_name'), sirname=request.POST.get('user_sirname'),
                                   secname=request.POST.get('user_secname'), phone=request.POST.get('user_phone'),
                                   country=request.POST.get('user_country'))
    return render(request, 'shop/user_info_setting.html', locals())


def pomosh(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/pomosh.html', locals())


def kak_sdelat_zakaz(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/kak-sdelat-zakaz.html', locals())


def vozvrat_i_obmen_tovara(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/vozvrat_i_obmen_tovara.html', locals())


def sposoby_oplaty(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/sposoby_oplaty.html', locals())


def informatsiya(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/informatsiya.html', locals())


def sertifikaty(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/sertifikaty.html', locals())


def vakansii(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/vakansii.html', locals())


def uslugi(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/uslugi.html', locals())


def dostavka(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/dostavka.html', locals())


def aktsii(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/aktsii.html', locals())


def kontakty(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/kontakty.html', locals())


def uspeh(request):
    mail_form = MailingForms()
    if "emaill" in request.POST:
        Mailig.objects.create(email=request.POST.get("emaill"))
    return render(request, 'shop/uspeh.html', locals())

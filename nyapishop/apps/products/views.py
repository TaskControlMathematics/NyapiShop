from django.shortcuts import render
from .models import *
# from shop.forms import MailingForm
from .forms import *
from django.contrib.auth import authenticate,login


def product(request, product_id):
    category_queryset = list(Categories.objects.all())
    all_slugs = [x.category for x in category_queryset]
    category = Product.objects.get(id=product_id).product_id_category
    print(category)
    parent = category.id_parent
    catalog_string = str(category).split(' -> ')
    lst = []
    for value in catalog_string:
        if value in all_slugs:
            lst.append(Categories.objects.get(category=value).id)
    trees = zip(catalog_string[:-1], lst[:-1])
    qwe = zip(catalog_string[2:-1],lst[2:-1])
    catalog_name = catalog_string[-1]


    product_info = Product.objects.get(id=product_id)
    # print(product_info.product_tree_catalog)
    tree_razdels = product_info.product_tree_catalog.split('/')
    razdels = []
    for i in range(1,len(tree_razdels) - 1 ):
        razdels.append(tree_razdels[i])
    print(razdels)


    session_key = request.session.session_key
    mail_form = Mailing(request.POST or None)
    form = AuthUserForm(request.POST or None)
    comment_form = CommentForm(request.POST or None)

    if not session_key:
        request.session.cycle_key()
    if request.method == "POST":
        if "password" in request.POST:
            # if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print(user)
            # if user is not None:
            login(request, user)
        elif "emaill" in request.POST :
            Mailig.objects.create(email=request.POST.get("emaill"))
        elif "comment_text" in request.POST:
            Comment.objects.create(product=product_info, comment_text=request.POST.get("comment_text"))
            # form = MailingForms(request.POST)

    else:
        form = AuthUserForm()

    return render(request, 'products/product.html', locals())



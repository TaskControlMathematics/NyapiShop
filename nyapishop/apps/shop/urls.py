from django.urls import path,include
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.main, name='main'),
    path('p/<int:main_page>', views.main_with_page, name='main_with_page'),
    path('catalog/<int:id_category>', views.catalog_first, name='catalog_first'),
    path('catalog/<int:id_category>/p/<int:catalog_page>', views.catalog_with_page, name='catalog_with_page'),
    path('registration',views.registred,name='registred'),
    path('user_agreement/', views.user_agreement, name='user_agreement'),
    path('auth',views.auth,name ="auth"),
    path('password_forgot',views.password_forgot,name="password_forgot"),
    path('user_info',views.user_info, name = "user_info"),
    path('user_info_setting',views.user_info_setting, name = 'user_info_setting'),
    path('pomosh',views.pomosh,name='pomosh'),
    path('kak_sdelat_zakaz',views.kak_sdelat_zakaz,name='kak_sdelat_zakaz'),
    path('vozvrat_i_obmen_tovara',views.vozvrat_i_obmen_tovara,name='vozvrat_i_obmen_tovara'),
    path('sposoby_oplaty',views.sposoby_oplaty,name='sposoby_oplaty'),
    path('informatsiya',views.informatsiya,name='informatsiya'),
    path('sertifikaty',views.sertifikaty,name='sertifikaty'),
    path('vakansii',views.vakansii,name='vakansii'),
    path('uslugi',views.uslugi,name='uslugi'),
    path('dostavka',views.dostavka,name='dostavka'),
    path('aktsii',views.aktsii,name='aktsii'),
    path('kontakty',views.kontakty,name='kontakty'),
    path('eto_uspeh',views.uspeh,name='uspeh')

    # path('catalog/main/<str:first_catalog_name>', views.first_catalog_first, name='first_catalog_first'),
    # path('catalog/main/anime/<str:second_catalog_name>',views.second_catalog_first,name='second_catalog_first'),
    # path('registration',views.RegisterFormView.as_view())
]
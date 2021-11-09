from django.contrib import admin
from .models import *
from orders.models import Order
from django.contrib.auth.models import User


class OrdersInline(admin.TabularInline):
    model = Order


class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    inlines = [OrdersInline]

    class Meta:
        model = Profile

# admin.site.register(Mailing)
# admin.site.register(ProductAdminReg)
admin.site.register(Profile,ProfileAdmin)

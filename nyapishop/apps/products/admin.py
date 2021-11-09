from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    # prepopulated_fields={('name',)}

    class Meta:
        model = Categories

admin.site.register(ProductImage)
admin.site.register(Mailig)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(Categories,CategoryAdmin)
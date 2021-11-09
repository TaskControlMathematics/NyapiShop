from django.db import models
from phone_field import PhoneField
from products.models import Product,ProductImage
from shop.models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# class AuthCustomer(AuthenticationForm, models.Model):
#     class Meta:
#         model = User
#         fields = ("username", "password")
class Order(models.Model):
    user = models.ForeignKey(User, blank=True , null=True , default=None , on_delete=models.CASCADE)
    customer_snp = models.CharField(max_length=256)
    customer_email = models.EmailField()
    customer_phone = PhoneField(blank=True, help_text='Contact phone number')
    customer_other_information = models.TextField()
    customer_dostavka = models.TextField()
    total_price = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return "Заказ %s " % self.id

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    total_price = models.IntegerField(default=0)
    price_per_item = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.product.product_title

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def save(self, *args, **kwargs):
        price_per_item = self.product.product_price
        self.price_per_item = price_per_item

        self.total_price = self.count * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    order_total_price = 0
    all_products_in_order = ProductInOrder.objects.filter(order=order)
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    total_price = models.IntegerField(default=0)
    price_per_item = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    images = models.ForeignKey(ProductImage,blank=True, null=True,on_delete=models.CASCADE)

    # def __str__(self):
    #    return "%s" % self.product.product_title

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def save(self, *args, **kwargs):
        price_per_item = int(self.product.product_price)
        self.price_per_item = price_per_item

        self.total_price = int(self.count) * self.price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)

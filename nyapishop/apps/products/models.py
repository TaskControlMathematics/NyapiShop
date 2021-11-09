from django.db import models


class Mailig(models.Model):
    email = models.CharField(max_length=256)


class Categories(models.Model):
    category = models.TextField()
    id_parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        full_path = [self.category]
        k = self.id_parent
        while k is not None:
            full_path.append(k.category)
            k = k.id_parent
        return ' -> '.join(full_path[::-1])



class Product(models.Model):
    product_title = models.CharField("product_title", max_length=200)
    product_link = models.TextField()
    product_price = models.IntegerField()
    product_availability = models.BooleanField(default=True)
    product_catalog = models.CharField(max_length=50)
    product_tree_catalog = models.TextField()
    product_description = models.TextField()
    product_link_image = models.TextField()
    product_id_category = models.ForeignKey(Categories,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s " % self.product_title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["product_price",'product_title']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_main_image = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_text = models.TextField()




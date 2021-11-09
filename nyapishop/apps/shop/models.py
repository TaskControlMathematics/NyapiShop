from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField


# class admin_registrated(models.Model):
#     comment = models.TextField()


class Mailing(models.Model):
    email = models.EmailField()

    def __str__(self):
        return "%s " % self.email


class PasswordForgot(models.Model):
    email = models.CharField(max_length=256)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField(max_length=70,blank=True)
    name = models.CharField(max_length=500, blank=True)
    sirname = models.CharField(max_length=300, blank=True)
    secname = models.CharField(max_length=300, blank=True)
    phone = PhoneField(blank=True)
    comment = models.TextField(blank=False)
    country = models.CharField(max_length=70, blank=False)

    def __str__(self):
        return "%s " % self.user


@receiver(post_save, sender=User)
def new_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

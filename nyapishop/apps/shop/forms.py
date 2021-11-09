from django import forms
from .models import *
from products.models import Mailig
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField


class MailingForms(forms.ModelForm):
    emaill = forms.CharField()
    class Meta:
        model = Mailig
        fields = ('emaill',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].widget.attrs['class'] = 'email_form'
        self.fields['emaill'].widget.attrs['placeholder'] = 'E-mail*'
        self.fields['emaill'].widget.attrs['class'] = 'email_field'


class FilterForm(forms.Form):
    ordering = forms.ChoiceField(label="Сортировать по:", required=False, choices=[
        ['no_ordering','умолчанию'],
        ["product_price_min", "цене: убывание"],
        ["product_price_max", "цене: возрастание"],
        ["product_title_min", "названию: А-Я"],
        ["product_title_max" , "названию: Я-А"]
    ])
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'filter_form'


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'authlist'
        self.fields['username'].widget.attrs['placeholder'] = 'sample@domail.ru'
        self.fields['password'].widget.attrs['placeholder'] = '********'


class PasswordForgot(forms.ModelForm):
    emailqe = forms.CharField()

    class Meta:
        model = PasswordForgot
        fields = ('email',)


class SignUpForm(UserCreationForm):
  name = forms.CharField()
  sirname = forms.CharField()
  secname = forms.CharField()
  phone = PhoneNumberField(widget=forms.TextInput())
  comment = forms.CharField(widget=forms.Textarea())
  country = forms.CharField()
  class Meta:
     model = User
     fields = ('username', 'password1', 'password2','name','sirname','secname','phone','comment','country' )

class PriceFilterForm(forms.Form):
    price_left = forms.IntegerField(required=False)
    price_right = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'price_filter_input'

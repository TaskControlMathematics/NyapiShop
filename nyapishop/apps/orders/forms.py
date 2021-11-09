from django import forms
from .models import *
from products.models import Mailig
from phone_field import PhoneField


class CheckoutContactForm(forms.Form):
    snp = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.CharField(required=True)
    other = forms.CharField(required=True)
    dostavka = forms.CharField(required=True)


class MailingFormsOrder(forms.ModelForm):
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

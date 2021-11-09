from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField


class Mailing(forms.ModelForm):
    emaill = forms.CharField()
    class Meta:
        model = Mailig
        fields = ('emaill',)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # for field in self.fields:
        #     self.fields[field].widget.attrs['class'] = 'email_form'
        self.fields['emaill'].widget.attrs['placeholder'] = 'E-mail*'
        self.fields['emaill'].widget.attrs['class'] = 'email_field'



class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'myphiledauth'
        self.fields['username'].widget.attrs['placeholder'] = 'Введите Ваш e-mail'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите Ваш пароль'

class CommentForm(forms.ModelForm):
    comment_text = forms.Textarea()

    class Meta:
        model = Comment
        fields = ('comment_text',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['comment_text'].widget.attrs['placeholder'] = 'Комментарий:*'
        self.fields['comment_text'].widget.attrs['class'] = 'comment_text_area'


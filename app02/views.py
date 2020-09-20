from django.shortcuts import render

# Create your views here.

from django import forms
from app02 import models
from django.core.validators import RegexValidator


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='Phone',
                                   validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号码格式错误'), ])
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput())

    class Meta:
        model = models.UserInfo
        fields = "__all__"


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})

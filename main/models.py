
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.db import models
from django.urls import reverse
from django.db import models
# Create your models here.


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

    username = forms.CharField(required=True, min_length=3, max_length=15, widget=forms.TextInput(attrs={"autofocus": True}), strip=False,)
    email = forms.EmailField(required=True, min_length=7, widget=forms.EmailInput(attrs={"autocapitalize": "none", }))
    password1 = forms.CharField(required=True, min_length=8, widget=forms.PasswordInput())
    # password2 = forms.CharField(required=True, widget=forms.PasswordInput())
    # username = forms.CharField(required=True, min_length=3, max_length=20, widget=forms.TextInput(attrs={'class': 'comment', 'placeholder': 'Enter your username'}))
    # email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'comment', 'placeholder': 'Enter your email'}))
    # password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'comment', 'placeholder': 'Enter your password'}))
    # password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'comment', 'placeholder': 'Repeat your password'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        # fields = ['username', 'email', 'password1']

class Login_form(AuthenticationForm):
    username = forms.CharField(required=True, min_length=3, max_length=15, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'comment', 'placeholder': 'Enter your username'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'comment', 'placeholder': 'Enter your password'}))


class Media_models(models.Model):
    name = models.CharField('Name', max_length=50)
    title = models.TextField('Title')
    data_time_create = models.DateTimeField(auto_now_add=True)
    data_time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='Association')
    geeks_field = models.BooleanField()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-data_time_update', 'title', 'name']

class Comments(models.Model):
    name = models.CharField('Name',max_length=50)
    title = models.TextField()
    data_time = models.DateTimeField(auto_now_add=True,blank=True)
    user_comment = models.ForeignKey(Media_models,on_delete=models.CASCADE,default=None,verbose_name='Model_ID')
    slug = models.SlugField(max_length=255,db_index=True, verbose_name='Association')
    geeks_field = models.BooleanField()


    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-data_time', 'name']

from django import forms
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from .models import Media_models, Comments
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.core.exceptions import ValidationError


class addTasks(ModelForm):
    class Meta:
        model = Media_models
        fields = ['title']

        widgets = {
            'title': Textarea(attrs={
                'class': 'mailinglist-textfield textfield is-large is-white',
                'id': "mailinglist-textfield-password",
                'style': "height: 40px; width: 60%",
                'placeholder': 'Enter name your project'})
                   }

class editTasks(ModelForm):
    class Meta:
        model = Media_models
        fields = ['id', 'title']

        widgets = {
            'id': Textarea(attrs={
                'class': 'mailinglist-textfield textfield is-large is-white',
                'id': "mailinglist-textfield-password",
                'style': "height: 80px; width: 90%",
                'placeholder': 'Enter your Tasks'}),
            'title': Textarea(attrs={
                'class': 'mailinglist-textfield textfield is-large is-white',
                'id': "mailinglist-textfield-password",
                'style': "height: 80px; width: 90%",
                'placeholder': 'Enter your Tasks'})
                   }

class Comments_form(ModelForm):
    class Meta(Comments):
        model = Comments
        fields = ['title']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter your name'}),
            'title': Textarea(attrs={
                'class': 'mailinglist-textfield textfield is-large is-white',
                'id': "mailinglist-textfield-password",
                'style': "margin-bottom: 1em !important; margin-left: auto; height: 40px; width: auto;",
                'placeholder': 'Enter your Tasks'})
                   }

class Comments_form_EDITtask(ModelForm):
    class Meta(Comments):
        model = Comments
        fields = ['id', 'title']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter your name'}),
            'id': Textarea(attrs={
                'class': 'mailinglist-textfield textfield is-large is-white',
                'id': "mailinglist-textfield-password",
                'style': "height: 80px; width: 90%",
                'placeholder': 'Enter your Tasks'}),
            'title': Textarea(attrs={
                'class': 'mailinglist-textfield textfield is-large is-white',
                'id': "mailinglist-textfield-password",
                'style': "margin-bottom: 1em !important; margin-left: auto; height: 40px; width: auto;",
                'placeholder': 'Enter your Tasks'})
                   }



# class RegisterForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'comment', 'placeholder': 'Enter your username'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'comment', 'placeholder': 'Enter your email'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'comment', 'placeholder': 'Enter your password'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'comment', 'placeholder': 'Repeat your password'}))
#
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']
#
# class Login_form(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'comment', 'placeholder': 'Enter your username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'comment', 'placeholder': 'Enter your password'}))


def get_mod(data):
    try:
        return Media_models.objects.get(slug=data)
    except Exception:
        return False
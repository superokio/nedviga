from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='придумайте никнейм')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='придумайте пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='повторите пароль')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='введите ваше имя')
    avatar = forms.ImageField(widget=forms.FileInput(), label='Выберите фото профиля')

    class Meta:
        model = Profile
        fields = ['full_name', 'avatar']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Никнейм')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Пароль')

    class Meta:
        model = User
        fields = ['username', 'password']
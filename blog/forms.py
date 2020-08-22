from django import forms
from .models import MessagePost
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class UserLoginForm(AuthenticationForm):
	# Форма авторизации 
	username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'from-control'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'from-control'}))

class UserRegisterForm(UserCreationForm):
	# Форма регистрации 
	username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'from-control'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'from-control'}))
	password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'from-control'}))
	email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'from-control'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class MessagePostForm(forms.ModelForm):
	# Форма для поста 
	class Meta:
		model = MessagePost
		exclude = [""]
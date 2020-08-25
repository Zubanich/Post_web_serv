from django.shortcuts import render, redirect
from .models import *
from .forms import MessagePostForm, UserRegisterForm, UserLoginForm 
from django.http import HttpResponseRedirect
import datetime 
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login, logout
# Create your views here.

def register(request):
	# Функция для представления регистрации и формы регистрации
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Вы успешно зарегестрировались !')
			return redirect('blog')
		else:
			messages.error(request, 'Ошибка регистрации !')
	else:
		form = UserRegisterForm()
	return render(request, 'blog/register.html', locals())


def user_login(request):
	# Функция для представленя авторизации и формы авторизации 
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('blog')
	else:
		form = UserLoginForm()
	return render(request, 'blog/login.html', locals())


def user_logout(request):
	# Функция для выхода из аккаунта 
	logout(request)
	return redirect('blog')


def blog(request):
	# Функция для представления главной страницы проекта  
	posts = MessagePost.objects.all()

	need_type_sorted = '2' # Данные для типа сортировки постов ( По умолчанию от нового к старому) 

	if(request.method == 'POST'): # Если запрос типа POST, то берем данные для типа сортировки из dropdown  
		data = request.POST
		need_type_sorted = data['data']

	if need_type_sorted == '1': # Если тип сортировки '1' (от старого к новому) сортируем соответственно 
		posts = posts.order_by('create')

	if need_type_sorted == '2': # Если тип сортировки '2' (от нового к старому) сортируем соответственно 
		posts = posts.order_by('-create')

	now_time = timezone.now() # Берем текущее время
	need_start = now_time - datetime.timedelta(hours=24) # Отнимаем 24 часа от текущего времени 

	if need_type_sorted == '3': # Если тип сортировки '3' (все за последние 24 часа) сортируем соответственно 
		posts = posts.filter(create__gte=need_start) # Выбираем все посты время публикации каких больше или равно времени которое нашли в 2 строчках выше 

	return (render(request, 'blog/blog.html', locals())) 

def author(request, author_id):
	posts = MessagePost.objects.all()
	posts = posts.filter(id=author_id)
	name = posts[0].name
	all_posts_author = MessagePost.objects.filter(name=name)
	return render(request, 'blog/author.html', locals())

def formpost(request):
	# Функция для представления страницы создания поста и формы создания поста 
	form = MessagePostForm()
	return (render(request, 'blog/formpost.html', locals()))

def createpost(request):
	#  Функция для сохранения поста 
	if request.method == 'POST':
		form = MessagePostForm(request.POST, request.FILES)
		if form.is_valid():
			new_form = form
			new_form.save()

	posts = MessagePost.objects.all()
	return HttpResponseRedirect('/') # Редирект на главную страницу с постами 



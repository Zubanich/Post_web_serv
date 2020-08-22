from django.contrib import admin
from .models import *

# Register your models here.
class MessagePostAdmin(admin.ModelAdmin):
	# Настройка и подключение модели MessagePost в админку 
	list_display = [field.name for field in MessagePost._meta.fields]

	class Meta:
		model = MessagePost

admin.site.register(MessagePost, MessagePostAdmin)
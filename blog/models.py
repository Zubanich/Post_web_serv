from django.db import models

# Create your models here.

class MessagePost(models.Model):
	# Модель для поста 
	name = models.CharField(max_length=100, blank=True, null=True, default=None)
	userpost = models.TextField(blank=True, null=True, default=None)
	image = models.ImageField(null=True, upload_to='media/')
	create = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return "%s" % (self.name)

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
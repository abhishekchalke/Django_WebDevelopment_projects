from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings 


class Article(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE,)
	#author = models.CharField(max_length=50)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('article_detail', args=[str(self.id)])




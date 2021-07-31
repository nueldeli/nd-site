from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
	date_written = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200)
	post_snippet = models.CharField(max_length=250)
	thumbnail_img = models.ImageField("Thumbnail", null=True, blank=True, upload_to='thumbnail_img/')
	content = RichTextUploadingField()

	class Meta:
		ordering = ['-date_written']

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('post_index') 

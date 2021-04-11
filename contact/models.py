from django.db import models
from django.urls import reverse

# Create your models here.
class Message(models.Model):
	date_sent = models.DateTimeField(auto_now_add=True)
	sender_name = models.CharField(max_length=100)
	sender_email = models.EmailField(max_length=100)
	sender_message = models.TextField()

	class Meta:
		ordering = ['-date_sent']

	def __str__(self):
		return str(self.date_sent) + ' | ' + self.sender_name

	def get_absolute_url(self):
		return reverse('message_sent')
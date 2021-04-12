from django.db import models
from django.urls import reverse

# Create your models here.
class Subscribe(models.Model):
	date_subscribed = models.DateTimeField(auto_now_add=True)
	subscriber_first_name = models.CharField(max_length=100)
	subscriber_last_name = models.CharField(max_length=100)
	subscriber_email = models.EmailField(max_length=100)

	class Meta:
		ordering = ['-date_subscribed']

	def __str__(self):
		return str(self.date_subscribed) + ' | ' + self.subscriber_email

	def get_absolute_url(self):
		return reverse('subscribe_done')

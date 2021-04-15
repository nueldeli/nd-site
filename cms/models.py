from django.db import models
from django.urls import reverse

# Create your models here.
CLOSED = 'CLOSED'
INTERESTED = 'INTERESTED'
ONGOING = 'ONGOING'

STATUS_CHOICES = (
	('CLOSED', 'Closed'),
	('INTERESTED', 'Interested'),
	('ONGOING', 'Ongoing')
)

class CustomerData(models.Model):
	date_enter = models.DateTimeField(auto_now_add=True)
	customer_first_name = models.CharField(max_length=100)
	customer_last_name = models.CharField(max_length=100)
	customer_phone_no = models.CharField(max_length=100)
	customer_email = models.EmailField(max_length=100)
	status = models.CharField(choices=STATUS_CHOICES, max_length=200, default=ONGOING)

	class Meta:
		ordering = ['-date_enter']

	def __str__(self):
		return str(self.date_enter) + ' | ' + self.customer_first_name + self.customer_last_name

	def get_absolute_url(self):
		return reverse('cms_index')
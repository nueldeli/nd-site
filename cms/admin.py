from django.contrib import admin
from .models import CustomerData

# Register your models here.
class CustomerDataAdmin(admin.ModelAdmin):
	list_display = ('date_enter', 'customer_first_name', 'customer_last_name', 'customer_phone_no', 'customer_email', 'status')

admin.site.register(CustomerData, CustomerDataAdmin)
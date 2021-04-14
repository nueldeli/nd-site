from django.contrib import admin
from .models import Subscribe

# Register your models here.
class SubscribeAdmin(admin.ModelAdmin):
	list_display = ('date_subscribed', 'subscriber_first_name', 'subscriber_last_name', 'subscriber_email')

admin.site.register(Subscribe, SubscribeAdmin)
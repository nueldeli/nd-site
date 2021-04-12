from django import forms
from .models import Subscribe
from django.utils.translation import gettext_lazy as _

class SubscribeForm(forms.ModelForm):
	class Meta:
		model = Subscribe
		fields = ('subscriber_first_name', 'subscriber_last_name', 'subscriber_email')

		widgets = {
			'subscriber_first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}),
			'subscriber_last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}),
			'subscriber_email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
		}

		labels = {
			'subscriber_first_name':_(''),
			'subscriber_last_name':_(''),
			'subscriber_email':_(''),
		}
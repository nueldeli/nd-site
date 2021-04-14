from django import forms
from .models import CustomerData
from django.utils.translation import gettext_lazy as _

class CustomerDataForm(forms.ModelForm):
	class Meta:
		model = CustomerData
		fields = ('customer_first_name', 'customer_last_name', 'customer_phone_no', 'customer_email', 'status')

		widgets = {
			'customer_first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}),
			'customer_last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}),
			'customer_phone_no':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Phone number'}),
			'customer_email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			'status':forms.RadioSelect()
		}

		labels = {
			'customer_first_name':_(''),
			'customer_last_name':_(''),
			'customer_phone_no':_(''),
			'customer_email':_(''),
			'status':_(''),
		}
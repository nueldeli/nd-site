from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import CustomerData
from .forms import CustomerDataForm

# Create your views here.
class CustomerIndexView(ListView):
	model = CustomerData
	template_name = 'cms/cms_index.html'

class CustomerDetailView(DetailView):
	model = CustomerData
	template_name = 'cms/cms_detail.html'

class CustomerFormView(CreateView):
	model = CustomerData
	form_class = CustomerDataForm
	template_name = 'cms/cms_form.html'

from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CustomerData
from .forms import CustomerDataForm, CustomerDataUpdateForm

# Create your views here.
def analytics_view(request):
	data_object = CustomerData.objects.all()
	total_customer_number = data_object.count()
	closed_number = data_object.filter(status__icontains='CLOSED').count()
	interested_number = data_object.filter(status__icontains='INTERESTED').count()
	ongoing_number = data_object.filter(status__icontains='ONGOING').count()
	label = ['Closed', 'Ongoing', 'Interested']
	data = [closed_number, ongoing_number, interested_number]
	return render(request, 'cms/cms_analytics.html', 
		{'total_customer_number':total_customer_number, 
		'closed_number':closed_number, 
		'interested_number':interested_number,
		'ongoing_number':ongoing_number,
		'label':label,
		'data':data
		})


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

class CustomerUpdateView(UpdateView):
	model = CustomerData
	form_class = CustomerDataUpdateForm
	template_name = 'cms/cms_update.html'

class CustomerDeleteView(DeleteView):
	model = CustomerData
	template_name = 'cms/cms_delete.html'
	success_url = reverse_lazy('cms_index')
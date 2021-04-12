from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import SubscribeForm
from .models import Subscribe

# Create your views here.
class SubscribeView(CreateView):
	model = Subscribe
	form_class = SubscribeForm
	template_name = 'landing/subscribe_form.html'

class SubscribeDoneView(TemplateView):
	template_name = 'landing/subscribe_done.html'
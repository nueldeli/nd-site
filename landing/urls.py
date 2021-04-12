from django.urls import path
from .views import SubscribeView, SubscribeDoneView

urlpatterns = [
	path('subscribe_form/', SubscribeView.as_view(), name='subscribe_form'),
	path('subscribe_done/', SubscribeDoneView.as_view(), name='subscribe_done'),
]
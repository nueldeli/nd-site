from django.urls import path
from .views import CustomerIndexView, CustomerDetailView, CustomerFormView

urlpatterns = [
	path('cms_index/', CustomerIndexView.as_view(), name='cms_index'),
	path('cms_detail/<int:pk>/', CustomerDetailView.as_view(), name='cms_detail'),
	path('cms_form/', CustomerFormView.as_view(), name='cms_form'),
]
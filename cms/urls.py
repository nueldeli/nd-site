from django.urls import path
from .views import analytics_view, CustomerIndexView, CustomerDetailView, CustomerFormView, CustomerUpdateView, CustomerDeleteView

urlpatterns = [
	path('cms_analytics/', analytics_view, name='cms_analytics'),
	path('cms_index/', CustomerIndexView.as_view(), name='cms_index'),
	path('cms_detail/<int:pk>/', CustomerDetailView.as_view(), name='cms_detail'),
	path('cms_form/', CustomerFormView.as_view(), name='cms_form'),
	path('cms_update/<int:pk>/', CustomerUpdateView.as_view(), name='cms_update'),
	path('cms_delete/<int:pk>/', CustomerDeleteView.as_view(), name='cms_delete'),
]
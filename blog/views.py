from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import AddPostForm, UpdatePostForm
from .models import Post 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class PostIndexView(ListView):
	model = Post
	template_name = 'blog/post_index.html'

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class PostAddView(CreateView):
	model = Post
	template_name = 'blog/post_add.html'
	form_class = AddPostForm

class PostUpdateView(UpdateView):
	model = Post
	template_name = 'blog/post_update.html'
	form_class = UpdatePostForm

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('post_index')
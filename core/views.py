# Arquivo: core/views.py

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# View para READ (List)
class PostListView(ListView):
    model = Post
    template_name = 'core/post_list.html'
    ordering = ['-created_at'] 

# View para READ (Detail)
class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'

# View para CREATE
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'core/post_form.html'
    success_url = reverse_lazy('post_list')

# View para UPDATE
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'core/post_form.html'
    success_url = reverse_lazy('post_list') 

# View para DELETE
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'core/post_confirm_delete.html' 
    success_url = reverse_lazy('post_list')
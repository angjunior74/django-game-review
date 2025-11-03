# Arquivo: core/views.py

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# View para READ (List)
class PostListView(ListView):
    model = Post
    template_name = 'core/post_list.html'
    ordering = ['-created_at'] 

# View para READ (Detail)
class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm() 
        return context

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
    
    
@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        return redirect('post_detail', pk=post.pk)
    
    
class CategoryListView(ListView):
    model = Category
    template_name = 'core/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'core/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all().order_by('-created_at')
        return context
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
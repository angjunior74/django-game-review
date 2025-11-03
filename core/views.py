# Arquivo: core/views.py

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

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
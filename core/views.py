# Arquivo: core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# READ (List)
def post_list(request):
    posts = Post.objects.all().order_by('-created_at') # Ordena pela data
    return render(request, 'core/post_list.html', {'object_list': posts})

# READ (Detail)
def post_detail(request, pk):
    # Responde 404 caso o post não exista
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'core/post_detail.html', {'post': post})

# CREATE
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm() 

    return render(request, 'core/post_form.html', {'form': form})

# UPDATE
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post) 

    return render(request, 'core/post_form.html', {'form': form, 'post': post})

# DELETE
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        # Se o formulário de confirmação for enviado
        post.delete()
        return redirect('post_list')
    
    # Se for um GET, apenas mostra a página de confirmação
    return render(request, 'core/post_confirm_delete.html', {'post': post})
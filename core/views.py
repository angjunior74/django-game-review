# Arquivo: core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

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
        # Pega os dados direto do formulário, sem validação
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('post_list')
    
    # Se for um GET, apenas mostra o formulário vazio
    return render(request, 'core/post_form.html')

# UPDATE
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_detail', pk=post.pk)
    
    # Se for um GET, mostra o formulário preenchido com dados do post
    return render(request, 'core/post_form.html', {'post': post})

# DELETE
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        # Se o formulário de confirmação for enviado
        post.delete()
        return redirect('post_list')
    
    # Se for um GET, apenas mostra a página de confirmação
    return render(request, 'core/post_confirm_delete.html', {'post': post})
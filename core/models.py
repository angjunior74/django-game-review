from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título do Jogo")
    content = models.TextField(verbose_name="Avaliação") # Armazenará HTML
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Postagem")

    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data da postagem")

    def __str__(self):
        return self.text[:50]
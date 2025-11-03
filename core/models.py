from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Gênero")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título do Jogo")
    content = models.TextField(verbose_name="Avaliação")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Postagem")
    categories = models.ManyToManyField(Category, related_name='posts', verbose_name="Gêneros")

    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data da postagem")

    def __str__(self):
        return self.text[:50]
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título do Jogo")
    content = models.TextField(verbose_name="Avaliação") # Armazenará HTML
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Postagem")

    def __str__(self):
        return self.title

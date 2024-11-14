from django.db import models


class ContentBlock(models.Model):
    image = models.ImageField(upload_to='content_images/', blank=True, null=True)
    description = models.TextField()  # Полное описание для второй страницы
    short_description = models.CharField(max_length=200, blank=True, null=True)  # Краткое описание для первой страницы
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.description[:20]


class Post(models.Model):
    title = models.CharField(max_length=200)  # Убедитесь, что это поле существует
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Post2(models.Model):
    title = models.CharField(max_length=200)  # Убедитесь, что это поле существует
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

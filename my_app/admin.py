from django.contrib import admin
from .models import Post2
from django.contrib import admin
from .models import ContentBlock, Post

class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('description', 'short_description', 'image')
    fields = ('description', 'short_description', 'image', 'button_text', 'button_url')

admin.site.register(ContentBlock, ContentBlockAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

admin.site.register(Post, PostAdmin)

admin.site.register(Post2)



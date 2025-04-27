from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'preview', 'created_at', 'sign_of_publication', 'views_count',)
    search_fields = ('title', 'content',)
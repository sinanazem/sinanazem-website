from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","slug","status","publish"]
    search_fields = ["title", "content", "abstract"]

admin.site.register(Article, ArticleAdmin)

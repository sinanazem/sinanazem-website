from django.shortcuts import render

from django.shortcuts import render
from django.views import View
from .models import Article





class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, "blogs/blog_list.html",{"articles":articles})
    

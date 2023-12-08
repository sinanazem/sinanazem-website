from django.shortcuts import render
from .models import Article



def home(requests):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(requests, "blog/index.html", context=context)

def about(requests):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(requests, "blog/about.html", context=context)


def contact(requests):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(requests, "blog/contact.html", context=context)

def detail(requests, post_id):
    article = Article.objects.get(pk=post_id)
    context = {"article": article}
    return render(requests, "blog/post.html", context=context)

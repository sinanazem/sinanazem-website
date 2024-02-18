from django.urls import path
from .views import ArticleView

app_name = "blog"
urlpatterns = [
    path('', ArticleView.as_view(), name='blog'),
]
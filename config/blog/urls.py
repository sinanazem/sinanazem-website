from django.contrib import admin
from django.urls import path
from .views import home, detail

app_name = "blog"
urlpatterns = [
    path('', home, name="blog"),
    path('<int:post_id>/', detail),
]

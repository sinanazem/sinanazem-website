from django.contrib import admin
from django.urls import path
from .views import home, detail, about, contact

app_name = "blog"
urlpatterns = [
    path('', home, name="blog"),
    path('<int:post_id>/', detail),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

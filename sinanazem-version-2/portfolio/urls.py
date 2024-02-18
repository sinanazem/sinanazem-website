from django.urls import path
from .views import PortfolioView

app_name = "portfolio"
urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
]
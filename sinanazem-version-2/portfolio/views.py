from django.shortcuts import render
from django.views import View


class PortfolioView(View):
    def get(self, request):
        return render(request, 'portfolio/portfolio.html')

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageViews(TemplateView):
    template_name = "home.html"


class CalculatorViews(TemplateView):
    template_name = "calculator.html"

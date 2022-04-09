from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def homePageViews(request):
    return HttpResponse("Salom Dunyo")


class HomePageViews(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class Calculator(TemplateView):
    template_name = "calculator.html"

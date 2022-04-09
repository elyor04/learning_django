# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PostModel

# Create your views here.
class BlogListView(ListView):
    model = PostModel
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = PostModel
    template_name = "detail.html"

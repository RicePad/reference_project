from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HelloView(TemplateView):
    template_name = "home.html"

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from blog.models import Blog


def list_all_blogs(request):
    blogs = Blog.objects.all
    return render(request, "blog_list.html", {"blogs": blogs})

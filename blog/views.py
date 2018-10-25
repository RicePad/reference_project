from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from blog.models import Blog


def list_all_blogs(request):
    blogs = Blog.objects.all
    return render(request, "blog_list.html", {"blogs": blogs})



def detail_blog(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog_detail.html", {"blog": detail_blog})

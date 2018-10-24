from django.urls import path
from blog import views

app_name = "blogs"

urlpatterns = [
    path('list', views.list_all_blogs, name="blog_list" )

]

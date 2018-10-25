from django.urls import path
from blog import views

app_name = "blogs"

urlpatterns = [
    path('', views.list_all_blogs, name="blog_list" ),
    path('list', views.list_all_blogs, name="blog_list" ),
    path('<int:blog_id>/',views.detail_blog, name="blog_detail")

]

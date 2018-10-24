from django.urls import path
from jobs import views

app_name = "jobs"

urlpatterns = [
    path('', views.find_job_list, name="job_list"),
]

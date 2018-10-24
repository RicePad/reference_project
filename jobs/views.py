from django.shortcuts import render
from jobs.models import Job

# Create your views here.

def find_job_list(request):
     jobs = Job.objects.all
     return render(request, 'job_list.html', {'jobs':jobs})

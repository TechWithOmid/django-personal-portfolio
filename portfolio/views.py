from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/home.html', context) 
from django.shortcuts import render
from .models import Project
def home(request):
    projectlist = Project.objects.all()
    return render(request, 'home.html',{'projectlist':projectlist})
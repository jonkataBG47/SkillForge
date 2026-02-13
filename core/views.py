from django.shortcuts import render
from django.http import HttpRequest
from skills.models import Skill
def home(request:HttpRequest):
    skills = Skill.objects.all().order_by('-created_at','title')
    context = {'skills':skills}
    return render(request,'core/home.html',context)
def about(request:HttpRequest):
    return render(request,'core/about.html')
def custom_404(request:HttpRequest, exception):
    return render(request,'404.html', status=404)


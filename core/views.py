from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView

from skills.models import Skill
def home(request:HttpRequest):
    if request.user.is_authenticated:
        skills = Skill.objects.filter(user=request.user).order_by('-created_at', 'title')
        context = {'skills': skills}
    else:
        context = {}
    return render(request,'core/home.html',context)
def about(request:HttpRequest):
    return render(request,'core/about.html')
def custom_404(request:HttpRequest, exception):
    return render(request,'404.html', status=404)
def custom_500(request):
    return render(request, '500.html', status=500)

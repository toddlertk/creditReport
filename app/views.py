# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from app.models import BlogPost
from django.shortcuts import render
from app import apps

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))

def app_login(request):
    c = Context({'name': apps.AppConfig.name})
    return render(request, 'login.html' , c)
    
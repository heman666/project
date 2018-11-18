from django.shortcuts import render,get_object_or_404
from practise.models import *
from practise.forms import Info_form
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,"index.html")

def index(request):
    if request.method == "POST":
        form = Info_form(request.POST)
        ob = Info.objects.all()
        if form.is_valid():
            form.save()
            return render(request,"index.html")
        else:
            print(form.errors)
    else:
        form = Info_form()
    return render(request,"index0.html",{'form':form})

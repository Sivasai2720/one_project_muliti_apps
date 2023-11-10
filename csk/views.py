from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return render(request,'msd.html') #By using rendering to html form.
def ravendra(request):
    return HttpResponse('<h1>All ROUNDER MR. Jadeja</h1>')
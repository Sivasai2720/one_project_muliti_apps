from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return render(request,'rcb.html')

def abd(request):
    return HttpResponse('<center><h1>MR LEFT SUPER BATSMAN</h1></center>')
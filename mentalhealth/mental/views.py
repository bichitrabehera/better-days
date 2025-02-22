from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def therapist(request):
    return render(request, 'therapist.html')

def resources(request):
    return render(request, 'resources.html')

def forum(request):
    return render(request, 'forum.html')
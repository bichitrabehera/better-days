from django.shortcuts import render, redirect
from .models import StudentExperience

def home(request):
    return render(request, 'index.html')


from django.shortcuts import render

def submit_experience(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        content = request.POST.get('content')
        StudentExperience.objects.create(username=username, content=content)
        return redirect('home')  # Redirect to home after submission

    return render(request, 'submit_experience.html')  # Render a form for submission

def display_experiences(request):
    experiences = StudentExperience.objects.all()
    return render(request, 'forum.html', {'experiences': experiences})


def therapist(request):
    return render(request, 'therapist.html')

def resources(request):
    return render(request, 'resources.html')

def forum(request):
    return render(request, 'forum.html')

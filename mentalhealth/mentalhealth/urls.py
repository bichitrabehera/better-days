from django.urls import path
from mental.views import home, therapist, resources, forum, submit_experience, display_experiences

urlpatterns = [
    path('', home, name='home'),
    path('therapist/', therapist, name='therapist'),
    path('resources/', resources, name='resources'),
    path('forum/', forum, name='forum'),
    path('submit_experience/', submit_experience, name='submit_experience'),
    path('display_experiences/', display_experiences, name='display_experiences'),
]

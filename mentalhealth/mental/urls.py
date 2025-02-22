from django.urls import path
from .views import home, therapist , resources , forum

urlpatterns = [
    path('', home, name='home'),
    path('therapist/', therapist, name='therapist'),
    path('resources/', resources, name='resources'),
    path('forum/', forum, name='forum')

]

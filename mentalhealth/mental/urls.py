from django.urls import path
from .views import home, therapist

urlpatterns = [
    path('', home, name='home'),
    path('therapist/', therapist, name='therapist'),
]

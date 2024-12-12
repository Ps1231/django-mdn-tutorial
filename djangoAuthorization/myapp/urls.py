from django.urls import path
from . import views  # Import your app's views module

urlpatterns = [
    path('', views.home, name='home'),  # Replace 'home' with your actual view function
]
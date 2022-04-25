
from django.shortcuts import render
from.models import Dog

# Add the following import
from django.http import HttpResponse


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Doggos</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs })
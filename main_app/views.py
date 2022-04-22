
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Brooklyn', 'Pitbull', 'boneless spare rib lover', 7),
  Dog('Monte', 'Corgi', 'Sock detective', 2),
  Dog('Miles', 'Cavapoo', 'Goodboy', .5)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Doggos</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })
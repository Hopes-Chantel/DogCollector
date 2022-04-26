
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from.models import Dog

# Add the following import
from django.http import HttpResponse


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Doggos</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dog = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dog })

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  return render(request, 'dogs/detail.html', { 'dog': dog })

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'
  success_url = '/dogs/'

class DogUpdate(UpdateView):
  model = Dog
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'
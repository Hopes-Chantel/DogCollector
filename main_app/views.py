
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from.models import Dog
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', { 'dog': dog, 'feeding_form': feeding_form })

def add_feeding(request, dog_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('detail', dog_id=dog_id)

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'
  success_url = '/dogs/'

class DogUpdate(UpdateView):
  model = Dog
  
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'
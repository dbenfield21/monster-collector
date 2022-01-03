from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

class Monster:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name):
    self.name = name
    

monsters = [
  Monster ("Chewy"),
  Monster ("Fred"), 
  Monster ("Aragog"),
  
]

def home(request):
  return HttpResponse('<h1>Hello Monsters</h1>')

def about(request):
  return render(request, 'about.html')

def monsters_index(request):
  return render(request, 'monsters/index.html', { 'monsters': monsters })
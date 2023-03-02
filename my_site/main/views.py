from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def base(response):
     return render(response, 'main/base.html', {"name": "test"})

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'main/list.html', {"ls": ls})

def home(response, name):
    my_dict = {"name": name}
    return render(response, 'main/home.html', my_dict)

def create(response):
    form = CreateNewList()
    return render(response, 'main/create.html', {"form": form})
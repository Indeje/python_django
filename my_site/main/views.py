from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def base(response):
     return render(response, 'main/base.html', {"name": "base"})


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":

        if response.POST.get("save"):

            for item in ls.item_set.all():

                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("newListItem")

            if len(txt) > 2:
                ls.item_set.create(name=txt, complete=False)
            else:
                print("Invalid. Enter 3 characters or more.")


    return render(response, 'main/list.html', {"ls": ls})


def home(response):
    #my_dict = {"name": name}
    return render(response, 'main/home.html', {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, 'main/create.html', {"form": form})

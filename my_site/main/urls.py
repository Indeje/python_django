from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create")
]

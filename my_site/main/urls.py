from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("<int:id>", views.index, name="index"),
    path("<str:name>", views.home, name="home")
]

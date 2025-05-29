from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("", views.home, name="home"),
    path("contato/", views.contato, name="contato"),
    path("curso/", views.curso, name="curso"),
    path("add-curso/", views.add_curso, name="add_curso"),
]

from django.urls import path
from . import views

app_name = 'app'  # Namespace para evitar conflitos

urlpatterns = [
    path('', views.home, name='home'),
    path('planos/', views.planos, name='planos'),
    path('contatos/', views.contatos, name='contatos'),
    path('add-produto/', views.add_produto, name='add_produto'),
]
from django.shortcuts import render, redirect
from .models import Curso
from django.conf import settings
from .forms import CursoForms, ProfileForm
import os 

def home(request):
    return render(request,'app/home.html',{'home':home})
def contato(request):
    return render(request,'app/contato.html',{'contato':contato})
def curso(request):
    '''
    View para listar curso disponíveis
    Filtra apenas curso marcados como disponíveis
    '''
    curso = Curso.objects.filter(disponivel=True)
    return render(request, 'app/curso.html', {'curso': curso})

def add_curso(request):
    '''
    View para adicionar novo Curso
    Manipula upload de imagem e validação do formulário
    '''
    if request.method == 'POST':
        form = CursoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('curso')
    else:
        form = CursoForms()
    return render(request, 'app/add_curso.html', {'form': form})

def upload_profile(request):
    '''
    View para upload de foto de perfil
    '''
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'app/upload_profile.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Produto
from django.conf import settings
from .forms import ProdutoForm, ProfileForm, ContatoForm
import os
from django.contrib import messages
from django.core.mail import send_mail
from .models import ServicoReforma



def home(request):
    return render(request, "app/home.html")


def produtos(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, "app/produtos.html", {"produtos": produtos})


def contatos(request):
    """Página de contato com formulário"""
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Salva a solicitação no banco
            solicitacao = form.save()
            
            # Envia email (opcional)
            try:
                send_mail(
                    subject=f'Nova solicitação: {solicitacao.assunto}',
                    message=f'''
                    Nova solicitação de contato recebida:
                    
                    Nome: {solicitacao.nome}
                    Email: {solicitacao.email}
                    
                    Mensagem:
                    {solicitacao.mensagem}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@reformas.com',
                    recipient_list=['contato@reformas.com'],  # Substitua pelo seu email
                )
            except Exception as e:
                print(f'Erro ao enviar email: {e}')
            
            messages.success(request, 'Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.')
            return redirect('app:contatos')
    else:
        form = ContatoForm()
    
    context = {
        'form': form
    }
    return render(request, 'app/contatos.html', context)


def list_profile_pics(request):
    """
    Lista todas as imagens de perfil usando a OS Library.
    """
    pics_path = os.path.join(settings.MEDIA_ROOT, "profile_pics")
    pictures = [f for f in os.listdir(pics_path) if f.endswith((".jpg", ".png"))]
    return render(request, "list_pics.html", {"pictures": pictures})


def add_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)  # Note o request.FILES!
        if form.is_valid():
            form.save()
            return redirect("lista_planos")
    else:
        form = ProdutoForm()
    return render(request, "app/add_produto.html", {"form": form})


def upload_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("home")
    else:
        form = ProfileForm()
    return render(request, "app/upload_profile.html", {"form": form})

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Modelo para produtos com imagem
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(
        upload_to="static/app/img",  # Salva em media/produtos/
        blank=True,  # Opcional
        null=True,  # Pode ser nulo
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="profile_pics/",  # Pasta dentro de MEDIA_ROOT
        default="profile_pics/default.jpeg",
    )
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class ContatoSolicitacao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    respondido = models.BooleanField(default=False)
    
    class Meta:
        verbose_name='solicitação de contato'
        verbose_name_plural='solicitações de contato'
        ordering = ['-data_envio']
        
    def __str__(self):
        return f'{self.nome} - {self.email}'
        
class ServicoReforma(models.Model):
    TIPOS_SERVICO = [
        ('pintura', 'Pintura'),
        ('eletrica', 'Elétrica'),
        ('hidraulica', 'Hidráulica'),
        ('alvenaria', 'Alvenaria'),
        ('pisos', 'Pisos e Revestimentos'),
        ('telhado', 'Telhados'),
        ('jardim', 'Jardins e Paisagismo'),
        ('completa', 'Reforma Completa'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_SERVICO)
    descricao = models.TextField()
    preco_base = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Serviço de Reforma'
        verbose_name_plural = 'Serviços de Reforma'

    def __str__(self):
        return self.nome






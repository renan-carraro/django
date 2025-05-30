from django import forms
from .models import Produto, UserProfile,ContatoSolicitacao

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "imagem", "preco"]  # Campos do formulário


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_pic"]  # Apenas o campo de foto

class ContatoForm(forms.ModelForm):
    class Meta:
        model = ContatoSolicitacao
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu.email@exemplo.com'
            }),
           
            'mensagem': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Descreva sua necessidade de reforma ou tire suas dúvidas...'
            })
        }
        labels = {
            'nome': 'Nome Completo',
            'email': 'E-mail',
            'mensagem': 'Mensagem'
        }

from django import forms
from .models import Curso, UserProfile,ContatoSolicitacao


class CursoForms(forms.ModelForm):
    # formulário para criação e edição de produtos
    class Meta:
        model = Curso
        fields = ["nome", "imagem", "preco", "disponivel"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={"class": "form-control"}),
        }


class ProfileForm(forms.ModelForm):
    # formulário para upload de foto de perfil
    class Meta:
        medel = UserProfile
        fields = ["foto", "bio"]
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

class ContatoForm(forms.ModelForm):
    class Meta:
        model = ContatoSolicitacao
        fields = ["nome", "email", "telefone", "assunto", "mensagem"]
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Seu nome completo"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "seu.email@exemplo.com"}
            ),
            "telefone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "(11) 99999-9999"}
            ),
            "assunto": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Assunto da sua solicitação",
                }
            ),
            "mensagem": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Descreva sua necessidade de reforma ou tire suas dúvidas...",
                }
            ),
        }
        labels = {
            "nome": "Nome Completo",
            "email": "E-mail",
            "telefone": "Telefone",
            "assunto": "Assunto",
            "mensagem": "Mensagem",
        }
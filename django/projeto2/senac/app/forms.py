from django import forms
from .models import Curso,UserProfile
class CursoForms(forms.ModelForm):
#formulário para criação e edição de produtos
    class Meta:
        model=Curso
        fields=['nome','imagem','preco','disponivel']
        widgets={
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'preco':forms.NumberInput(attrs={'class':'form-control'}),
        }
class ProfileForm(forms.ModelForm):
#formulário para upload de foto de perfil
    class Meta:
        medel=UserProfile
        fields=['foto','bio']
        widgets={
            "bio":forms.Textarea(attrs={'class':'form-control','rows':3}),
        }
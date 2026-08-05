from django import forms
from django.contrib.auth.models import User
from .models import Bairro, Ocorrencia

# Formulário de bairros
class BairroForm(forms.ModelForm):
    # Definimos os campos como CharField com TextInput para total controle de digitação
    latitude = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Ex: -9.4167'
        }),
        required=False,
        label="Latitude"
    )
    longitude = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Ex: -40.5000'
        }),
        required=False,
        label="Longitude"
    )

    class Meta:
        model = Bairro
        fields = ['nome', 'latitude', 'longitude']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: Centro, Santo Antônio'
            }),
        }

    # Validação e higienização do campo Nome (Requisito 7)
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome and len(nome.strip()) < 3:
            raise forms.ValidationError("O nome do bairro deve ter pelo menos 3 caracteres.")
        return nome.strip() if nome else nome

    # Converte qualquer vírgula para ponto e valida se é um float numérico válido
    def clean_latitude(self):
        val = self.cleaned_data.get('latitude')
        if val:
            val = val.replace(',', '.').strip()
            try:
                return float(val)
            except ValueError:
                raise forms.ValidationError("Informe um valor numérico válido para a latitude (Ex: -9.4167).")
        return None

    def clean_longitude(self):
        val = self.cleaned_data.get('longitude')
        if val:
            val = val.replace(',', '.').strip()
            try:
                return float(val)
            except ValueError:
                raise forms.ValidationError("Informe um valor numérico válido para a longitude (Ex: -40.5000).")
        return None
    
class OcorrenciaForm(forms.ModelForm):
    responsavel = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,
        empty_label="Selecione um responsável (Opcional)"
    )

    class Meta:
        model = Ocorrencia
        fields = ['bairro', 'descricao', 'data_hora', 'status', 'responsavel']
        widgets = {
            'bairro': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva a ocorrência'}),
            'data_hora': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responsavel'].label_from_instance = lambda obj: obj.get_full_name() or obj.username
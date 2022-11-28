from django import forms
from .models import Oferta

class CrearOferta(forms.ModelForm):
    nameTutor= forms.CharField(label='Nombre',
                        required=True,
                        widget=forms.TextInput(
                            attrs={
                                "placeholder": "Autor",
                                "class": "form-control",      
                                "id": "name",
                                "nameTutor": "nombre",
                                "size": "50",
                                "maxlength": "30"    
                            }))

    titulo= forms.CharField(label='Titulo',
                        required=True,
                        widget=forms.TextInput(
                            attrs={
                                "placeholder": "Titulo",
                                "class": "form-control",      
                                "id": "titulo",
                                "titulo": "titulo",
                                "size": "50",
                                "maxlength": "30"    
                            }))

    materia= forms.CharField(label='Materia',
                        required=True,
                        widget=forms.TextInput(
                            attrs={
                                "placeholder": "Materia",
                                "class": "form-control",      
                                "id": "materia",
                                "materia": "materia",
                                "size": "50",
                                "maxlength": "30"    
                            }))

    contacto=forms.CharField(label ='contacto',
                        required=True,
                        widget=forms.TextInput(
                            attrs={
                                "placeholder": "contacto",
                                "class":"form-control",
                                "id":"contacto",
                                "contacto":"contacto",
                                "size": "50",
                                "maxlength": "30" 
                            }))
    
    descripcion=forms.CharField(label ='Descripcion',
                        required=True,
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "Descripción de Oferta",
                                "class":"form-control",
                                "id":"descripcion",
                                "descripcion":"descripcion",
                                "size":"150",
                                "maxlength":"150"
                            }))

  

    class Meta:
        model = Oferta 
        fields = ['nameTutor','titulo','materia','contacto','descripcion'
    ]

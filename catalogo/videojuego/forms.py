from django import forms
from .models import Plataformas, VideoJuego

class PlataformasForms(forms.ModelForm):
    class Meta:
        model = Plataformas
        fields = ['marca','fabricante','tipo','generacion','capacidad_disco','gpu','soporte', 'web_oficial']
        labels = {
            'marca' : 'Marca',
            'fabricante' : 'Fabricante',
            'tipo' : 'Tipo',
            'generacion' : 'Generacion',
            'capacidad_disco' : 'Capacidad de disco',
            'gpu' : 'GPU',
            'soporte' : 'Soporte',
            'web_oficial' : 'Web oficial'

        }

        widgets = {

            'marca' : forms.TextInput(attrs={'class':'form-control'}),
            'fabricante' : forms.TextInput(attrs={'class':'form-control'}),
            'tipo' : forms.Select(attrs={'class':'form-control'}),
            'generacion' : forms.TextInput(attrs={'class':'form-control'}),
            'capacidad_disco' : forms.TextInput(attrs={'class':'form-control'}),
            'gpu' : forms.TextInput(attrs={'class':'form-control'}),
            'soporte' : forms.TextInput(attrs={'class':'form-control'}),
            'web_oficial' : forms.URLInput(attrs={'class':'form-control'}),
            
        }

class VideoJuegoForms(forms.ModelForm):

    class Meta:
        model = VideoJuego
        fields = [
            'nombre',
            'genero',
            'fabricante',
            'clasificacion',
            'ano_lanzamiento',
            'max_jugadores',
            'jugabilidad',
            'plataformas',
            'web_oficial',
            'imagen',
            'trailer',
            'ranking',
        ]
        labels = {

            'nombre' : 'Nombre',
            'genero' : 'Genero',
            'fabricante' : 'Fabricante',
            'clasificacion' : 'Clasificacion',
            'ano_lanzamiento' : 'Año de Lanzamiento',
            'max_jugadores' : 'Maximo de Jugadores',
            'jugabilidad' : 'Jugabilidad',
            'plataformas' : 'Plataformas',
            'web_oficial' : 'Web Oficial',
            'imagen' : 'Imagen',
            'trailer' : 'Trailer',
            'ranking' : 'Raking',

        }

        widgets = {

            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'genero' : forms.Select(attrs={'class':'form-control'}),
            'fabricante' : forms.TextInput(attrs={'class':'form-control'}),
            'clasificacion' : forms.Select(attrs={'class':'form-control'}),
            #'ano_lanzamiento' : forms.DateField(attrs={'class':'form-control'}),
            'ano_lanzamiento' : forms.DateInput(attrs={'type' : 'data', 'class':'form-control'}),
            'max_jugadores' : forms.TextInput(attrs={'class':'form-control'}),
            'jugabilidad' : forms.Select(attrs={'class':'form-control'}),
            'plataformas' : forms.CheckboxSelectMultiple(),
            'web_oficial' : forms.TextInput(attrs={'class':'form-control'}),
            'imagen' : forms.FileInput(),
            'trailer' : forms.TextInput(attrs={'class':'form-control'}),
            'ranking' : forms.TextInput(attrs={'class':'form-control'}),
        }
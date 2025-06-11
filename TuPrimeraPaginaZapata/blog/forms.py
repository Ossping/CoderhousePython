from django import forms
from .models import Categoria, Autor, Post

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class SearchForm(forms.Form):
    buscador = forms.CharField(label='Buscar', max_length=100)

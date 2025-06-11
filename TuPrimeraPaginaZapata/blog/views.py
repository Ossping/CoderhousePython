from django.shortcuts import render, redirect
from .forms import CategoriaForm, AutorForm, PostForm, SearchForm
from .models import Post

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/form_template.html', {'form': form, 'titulo': 'Crear Categoria'})

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/form_template.html', {'form': form, 'titulo': 'Crear Autor'})

def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/form_template.html', {'form': form, 'titulo': 'Crear Post'})

def buscar(request):
    form = SearchForm(request.GET or None)
    resultados = None
    if form.is_valid():
        query = form.cleaned_data['buscador']
        resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'blog/buscar.html', {'form': form, 'resultados': resultados})

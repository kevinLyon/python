from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Categoria
from.models import Anuncio


def home(request):
    categoria = Categoria.objects.all()
    ultimos_anuncios = Anuncio.objects.all()[:12]

    return render(request, 'home.html', {'categorias': categoria, 'anuncios': ultimos_anuncios})


def categoria(request, categoria_id):
    categoria_raw = get_object_or_404(Categoria,id=categoria_id)

    categorias = Categoria.objects.all()
    
    anuncios_filter = Anuncio.objects.filter(categoria=categoria_raw)

    return render(request, 'home.html', {'categorias': categorias, 'anuncios': anuncios_filter, 'categoria': categoria_raw})


def anuncio(request, anuncio_id):
    anuncio_obj = get_object_or_404(Anuncio, id=anuncio_id)

    categorias = Categoria.objects.all()

    return render(request, 'anuncio.html', {'categorias': categorias, 'anuncio': anuncio_obj})

from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Kniha, Zanr, Autor


def index(request):
    zanr = 'povídky'
    context = {
        'nadpis': zanr,
        'knihy': Kniha.objects.order_by('rok_vydani').filter(zanry__nazev=zanr),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)


class BookListView(ListView):
    model = Kniha
    template_name = 'books/book_list.html'
    queryset = Kniha.objects.order_by('-rok_vydani')
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Kniha
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class AuthorListView(ListView):
    model = Autor
    context_object_name = 'author_list'
    queryset = Autor.objects.annotate(pocet_knih=Count('kniha')).order_by('-pocet_knih')
    template_name = 'authors/author_list.html'


class AuthorDetailView(DetailView):
    model = Autor
    context_object_name = 'author'
    template_name = 'authors/author_detail.html'

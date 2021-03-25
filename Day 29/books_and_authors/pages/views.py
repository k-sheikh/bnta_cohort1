from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Author, Book
from .forms import NewAuthorForm


def index(request):
    return render(request, 'index.html')


def books_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'books.html', context)


def new_author_form(request):
    if request.method == 'GET':
        form = NewAuthorForm()
        return render(request, 'new_author.html', {'form': form})

    form = NewAuthorForm(request.POST)
    if not form.is_valid():
        return render(request, 'new_author.html', {'form': form})

    name = form.cleaned_data['name']
    year_of_birth = form.cleaned_data['year_of_birth']

    if Author.objects.filter(name=name):
        messages.warning(request, f'Author {name} already exists')
        return render(request, 'new_author.html', {'form': form})

    author = Author(name=name, year_of_birth=year_of_birth)
    author.save()

    return HttpResponseRedirect('books')


class ListBooksForAuthor(APIView):
    def get(self, request, format=None):
        author_id = request.GET.get('author_id')
        get_object_or_404(Author, pk=author_id)

        books = [
            {
                'title': book.title,
                'year_of_publication': book.year_of_publication,
                'copies_sold': book.copies_sold
            }
            for book in Book.objects.filter(author_id=author_id)
        ]
        return Response(books)


@login_required
def books_for_author(request):
    authors = Author.objects.all()
    return render(request, 'books_for_author.html', {'authors': authors})

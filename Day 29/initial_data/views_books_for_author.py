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


def books_for_author(request):
    authors = Author.objects.all()
    return render(request, 'books_for_author.html', {'authors': authors})

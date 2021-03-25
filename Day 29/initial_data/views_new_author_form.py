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

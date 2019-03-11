from django.shortcuts import render
from django.http import HttpResponse, Http404
from books.models import Book


# Create your views here.


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request.GET:
        error = False
        # massage = 'You searched for : %r' % request.GET['q']
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})

    return render(request, 'search_form.html', {'error': error})

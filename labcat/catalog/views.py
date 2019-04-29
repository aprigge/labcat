from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Book, Author
from .models import Publisher

class BookListView(ListView):
    model = Book
    def get_queryset(self):
            return self.model.objects.order_by('title')
    

class BookDetailView(DetailView):
    model = Book
    

class PublisherDetailView(DetailView):
    model = Publisher


class AuthorListView(ListView):
    model = Author
    
    def get_queryset(self):
        return self.model.objects.order_by('last_name')


def list(request):
    list = Publisher.objects.order_by('publisher_name')
    return render(request, 'catalog/PublisherList.html', {'publisherList': list})

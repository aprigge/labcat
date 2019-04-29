from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Book
from .models import Publisher

class BookListView(ListView):
	model = Book
	def get_queryset(self):
        	return self.model.objects.order_by('title')
	

class BookDetailView(DetailView):
	model = Book
	

class PublisherDetailView(DetailView):
	model = Publisher


def list(request):
	list = Publisher.objects.order_by('publisher_name')
	return render(request, 'catalog/PublisherList.html', {'publisherList': list})

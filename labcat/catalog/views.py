from django.shortcuts import render
from django.views.generic import DetailView

from .models import Book
from .models import Publisher


class BookDetailView(DetailView):
	model = Book
	
class PublisherDetailView(DetailView):
	model = Publisher

def list(request):
	list = Publisher.objects.order_by('publisher_name')
	return render(request, 'catalog/PublisherList.html', {'publisherList': list})
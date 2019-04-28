from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Book

class BookListView(ListView):
	model = Book
	def get_queryset(self):
        	return self.model.objects.order_by('title')
	
	
#class AuthorListView(ListView):
#	model = Author

class BookDetailView(DetailView):
	model = Book
	

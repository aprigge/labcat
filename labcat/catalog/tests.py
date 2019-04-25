from django.test import TestCase
from .models import Book, Publisher


class ModelsTestCase(TestCase):

	def setUp(self):
		book = Book.objects.create(
			title='Test Driven Development: By Example',
			barcode='12345678910',
			callnum='TX321.78 J42',
			volume='')

	def test_book_model(self):
		book = Book.objects.get(barcode='12345678910')
		self.assertEqual(repr(book), '<Book 1: Test Driven Development: By Example>')

class PublisherTestCase(TestCase):

	def setUp(self):
		publisher = Publisher.objects.create(
			publisher_name = 'Rizzoli',
			publisher_city = 'New York')

	def test_publisher_model(self):
		publisher = Publisher.objects.get(publisher_name='Rizzoli')
		self.assertEqual(repr(publisher), '<New York: Rizzoli')

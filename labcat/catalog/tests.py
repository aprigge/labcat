from django.test import TestCase
from .models import Book


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
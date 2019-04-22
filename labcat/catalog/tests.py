from django.test import TestCase
from .models import Book, Author


class ModelsTestCase(TestCase):
    def setUp(self):
        book = Book.objects.create(
            title='Test Driven Development: By Example',
            barcode='12345678910',
            callnum='TX321.78 J42',
            volume='')
        author = Author.objects.create(
            first_name='Joshua',
            middle_name='Bruin',
            last_name='Gomez')

    def test_book_model(self):
        book = Book.objects.get(barcode='12345678910')
        self.assertEqual(
            repr(book), '<Book 1: Test Driven Development: By Example>')

    def test_author_model(self):
        author = Author.objects.get(
            first_name='Joshua', middle_name='Bruin', last_name='Gomez')
        self.assertEqual(
            repr(author), '<Author 1: Joshua Bruin Gomez>')

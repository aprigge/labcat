from django.db import models


class Book(models.Model):
	title = models.CharField(max_length=256)
	volume = models.CharField(max_length=64, blank=True)
	callnum = models.CharField(max_length=32, blank=True)
	barcode = models.CharField(max_length=32, blank=True)

	def __repr__(self):
		return '<Book {}: {}>'.format(self.id, self.title)

class Publisher(models.Model):
	publisher_name = models.CharField(max_length=256)
	publisher_city = models.CharField(max_length = 64, blank=True)

	def __repr__(self):
		return '<{}: {}>'.format(self.publisher_city, self.publisher_name)

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    volume = models.CharField(max_length=64, blank=True)
    callnum = models.CharField(max_length=32, blank=True)
    barcode = models.CharField(max_length=32, blank=True)

    def __repr__(self):
        return '<Book {}: {}>'.format(self.id, self.title)


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32)

    def __repr__(self):
        return '<Author {}: {} {} {}>'.format(self.id, self.first_name, self.middle_name, self.last_name)

# Create your models here.

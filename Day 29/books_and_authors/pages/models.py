from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    year_of_birth = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} ({self.year_of_birth})'


class Book(models.Model):
    title = models.CharField(max_length=200)
    year_of_publication = models.IntegerField(default=0)
    copies_sold = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

from django.db import models


# Create your models here.

class Books(models.Model):
    EBOOK = 1
    PAPER = 2
    TYPE_BOOKS = (
        (EBOOK, 'e-Book'),
        (PAPER,'Paper book')
    )

    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    pages = models.PositiveIntegerField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    published = models.DateField(null=True, blank=True)
    visible = models.NullBooleanField(default=False)
    type_book = models.PositiveIntegerField(choices=TYPE_BOOKS)

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.title


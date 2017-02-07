from django.contrib import admin
from core.models import Books
from core.forms import BookForm


# Register your models here.
@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'type_book', 'price', 'pages',)
    list_filter = ('type_book', 'visible',)
    search_fields = ('__str__', 'author', 'description')

    form = BookForm

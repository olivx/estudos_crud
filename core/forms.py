from django import forms
from core.models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('author', 'title', 'description', 'pages', 'price',
               'published', 'visible', 'type_book')

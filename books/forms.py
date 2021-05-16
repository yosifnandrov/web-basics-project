from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'book_description': forms.Textarea(),
            'book_title': forms.TextInput,
            'book_pages': forms.NumberInput,
            'book_author': forms.TextInput,
        }

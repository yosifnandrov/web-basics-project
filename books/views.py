from django.shortcuts import render, redirect

# Create your views here.
from books.forms import BookForm
from books.models import Book


def index(request):
    context = {
        "books": Book.objects.all().order_by('book_title'),
    }
    return render(request, 'books/index.html', context)

def create_book(request):
    if request.method == "GET":
        context = {
            'form': BookForm(),
        }
        return render(request, 'books/create.html', context)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index books')

        context = {
            "form": form,
        }
        return render(request, 'books/create.html', context)


def edit_book(request,pk):
    book = Book.objects.get(pk=pk)

    if request.method == "GET":
        form = BookForm(instance=book)
        context = {
            "form": form,
        }
        return render(request, 'books/edit.html', context)
    else:
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('index books')
        context = {
            'form': form,
        }
        return render(request, 'books/edit.html', context)

def delete_book(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('index books')

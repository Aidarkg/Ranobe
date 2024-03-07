from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from book import models
from book import forms
from ebooklib import epub
import ebooklib


class BookListView(ListView):
    model = models.Book
    context_object_name = 'books'
    template_name = 'index.html'
    


def book_list_view(request):
    if request.method == 'GET':
        books = models.Book.objects.all()
        context = {'books': books}
        return render(
            request,
            'index.html',
            context
        )
    
def book_detail_view(request, id):
    if request.method == 'GET':
        book = models.Book.objects.get(id=id)
        context = {
            'book': book
        }
        return render(
            request,
            'book_detail.html',
            context
        )
    
def book_create_view(request):
    if request.method == "POST":
        form = forms.BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            print(form.errors)
    else:
        form = forms.BookCreateForm()
    return render(
        request,
        'create_book.html',
        {'form': form}
    )

def genre_list_view(request):
    if request.method == 'GET':
        genre = models.Genre.objects.all().order_by('name')
        context = {'genres': genre}
        return render(
            request,
            'genre.html',
            context
        )
    
def books_chapter_view(request, book_id, chapter_id):
    try:
        book = get_object_or_404(models.Book, id=book_id)
        book_chapter = get_object_or_404(models.BookFile, book_id=book)
        book_file_path = "media/" + str(book_chapter.file)

        book = epub.read_epub(book_file_path)

        chapter_content = None
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT and item.get_name() == f"Chapter{chapter_id}.html" :
                chapter_content = item.get_content().decode('utf-8')
                break
        
        if chapter_content is None:
            raise Http404('Chapter not found')

        chapter_content = chapter_content.replace('</h1>', '</h1><p>')
        chapter_content = chapter_content.replace('</body>', '</p></body>')

        next_chapter = chapter_id + 1
        if chapter_id != 1:
            previous_chapter = chapter_id - 1
        elif chapter_id == 1:
            previous_chapter = 1
        book_b = models.Book.objects.get(id=book_id)
        book_title = book_b.title
        context = {
            'chapter_content': chapter_content, 
            "next_chapter": next_chapter,
            "previous_chapter": previous_chapter,
            'book_id': book_id,
            'book_title': book_title
        }

        return render(
            request, 
            'book.html', 
            context
        )

    except models.Book.DoesNotExist:
        raise Http404('Book not found')
    except models.BookFile.DoesNotExist:
        raise Http404('Book file not found')
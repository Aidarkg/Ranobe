from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, CreateView, DetailView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db import IntegrityError
from book import models
from book import forms
from ebooklib import epub
import re
import ebooklib


class BookListView(LoginRequiredMixin, ListView):
    model = models.Book2
    context_object_name = 'books_2'
    template_name = 'books/book_list.html'
    login_url = '/login/'
    paginate_by = 5

    def get_context_data(self):
        context = super().get_context_data()
        queryset = self.get_queryset()
        paginator =  Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page', 1)
        page_ogj = paginator.get_page(page)
        context['max_page'] = page_ogj
        return context
    

class BookDetailView(LoginRequiredMixin, DetailView):
    model = models.Book2
    context_object_name = 'book_2'
    template_name = 'books/book_detail_2.html'
    pk_url_kwarg = 'id'
    login_url = '/login/'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = models.Book2
    form_class = forms.BookCreateForm
    template_name = 'books/create_book.html'
    success_url = '/'
    login_url = '/login/'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('file', 'Книга с таким заголовком уже существует.')
            return self.form_invalid(form)


class GenreListView(LoginRequiredMixin, ListView):
    model = models.Genre
    context_object_name = 'genres'
    template_name = 'books/genre.html'
    login_url = '/login/'


class BooksChapterView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, book_id, chapter_id):
        try:
            book = get_object_or_404(models.Book2, id=book_id)
            book_file_path = book.file.path

            book = epub.read_epub(book_file_path)

            chapter_content = None
            for item in book.get_items():
                chapter_number = re.sub(r'\D', '', item.get_name())
                if chapter_number.isdigit():
                    chapter_number = int(chapter_number)
                    if chapter_number == int(chapter_id):
                        if item.get_type() == ebooklib.ITEM_DOCUMENT:
                            chapter_content = item.get_content().decode('utf-8')
                            break
            
            number = 0
            for item in book.get_items():
                number += 1
            last_chapter_number = number -5


            if chapter_content is None:
                raise Http404('Chapter not found')
            chapter_content = chapter_content.replace('</h1>', '</h1><p>')
            chapter_content = chapter_content.replace('</body>', '</p></body>')

            next_chapter = int(chapter_id) + 1 if chapter_id < last_chapter_number else 1
            previous_chapter = int(chapter_id) - 1 if int(chapter_id) > 1 else last_chapter_number

            context = {
                'chapter_content': chapter_content, 
                "next_chapter": next_chapter,
                "previous_chapter": previous_chapter,
                'book_id': book_id,
                'book': book,
                'last_chapter': last_chapter_number
            }

            return render(
                request, 
                'books/book.html', 
                context
            )

        except models.Book.DoesNotExist:
            raise Http404('Book not found')
        except models.BookFile.DoesNotExist:
            raise Http404('Book file not found')


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Book2
    form_class = forms.BookCreateForm
    template_name = 'books/book_update.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('book_detail_2')
    login_url = '/login/'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Book2
    template_name = 'books/book_delete.html'
    pk_url_kwarg = 'id'
    success_url = '/'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_2'] = self.model.objects.get(pk=self.kwargs['id'])
        return context


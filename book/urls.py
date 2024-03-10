from django.urls import path
from book.views import BooksChapterView, BookUpdateView, BookDeleteView, \
     BookListView, BookDetailView, GenreListView, BookCreateView


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:id>/', BookDetailView.as_view(), name='book_detail_2'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('genre/', GenreListView.as_view()),
    path('book/<int:book_id>/<int:chapter_id>/', BooksChapterView.as_view(), name="book_chapters"),
    path('book/update/<int:id>', BookUpdateView.as_view(), name="book_update"),
    path('book/delete/<int:id>', BookDeleteView.as_view(), name="book_delete"),
]
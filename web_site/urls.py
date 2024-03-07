from django.contrib import admin
from django.urls import path
from book.views import book_list_view, book_detail_view, book_create_view, genre_list_view, books_chapter_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list_view, name='book_list'),
    path('book/<int:id>/', book_detail_view, name='book_detail'),
    path('book/create/', book_create_view),
    path('genre/', genre_list_view),
    path('book/<int:book_id>/<int:chapter_id>/', books_chapter_view, name="book_chapters"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

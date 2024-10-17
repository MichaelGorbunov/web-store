# students/urls.py
from django.urls import path

from library import views
from .views import BooksListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


app_name = 'library'

urlpatterns = [

    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),

    path('authors/', views.author_list, name='author_list'),
    path('authors2/', views.author_list_2, name='author_list2'),
]
# urlpatterns = [
#     path("books_list/", views.books_list, name="books_list"),
#     path("book_detail/<int:book_id>/", views.book_detail, name="books_detail"),
# ]


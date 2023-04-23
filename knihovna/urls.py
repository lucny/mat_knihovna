from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.BookListView.as_view(), name='books_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('authors', views.AuthorListView.as_view(), name='authors_list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
]

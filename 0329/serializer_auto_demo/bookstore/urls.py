from django.urls import path

from .views import api_overview, book_detail, book_list

urlpatterns = [
    path('', api_overview, name='api-overview'),
    path('books/', book_list, name='book-list'),
    path('books/<int:book_id>/', book_detail, name='book-detail'),
]

from datetime import date

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book


class BookAPITests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='深入理解序列化器',
            author='王五',
            price='79.90',
            published_date=date(2024, 3, 20),
            is_featured=True,
        )

    def test_overview_endpoint(self):
        response = self.client.get(reverse('api-overview'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('flow', response.data)
        self.assertEqual(response.data['endpoints']['book_list'], '/api/books/')

    def test_book_list_serializes_queryset(self):
        response = self.client.get(reverse('book-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], self.book.title)
        self.assertEqual(response.data['results'][0]['price'], '79.90')
        self.assertEqual(response.data['results'][0]['stock_label'], '推荐阅读')

    def test_book_detail_serializes_single_object(self):
        response = self.client.get(reverse('book-detail', args=[self.book.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result']['author'], self.book.author)
        self.assertEqual(response.data['result']['display_title'], str(self.book))

    def test_book_detail_returns_404_for_missing_book(self):
        response = self.client.get(reverse('book-detail', args=[999]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

from datetime import date

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


def seed_demo_books():
    if Book.objects.exists():
        return

    Book.objects.bulk_create(
        [
            Book(
                title='Django REST Framework 实战',
                author='张三',
                price='88.00',
                published_date=date(2024, 5, 1),
                is_featured=True,
            ),
            Book(
                title='Python Web 接口设计',
                author='李四',
                price='66.50',
                published_date=date(2023, 9, 15),
                is_featured=False,
            ),
        ]
    )


@api_view(['GET'])
def api_overview(request):
    return Response(
        {
            'message': '这个项目用于演示 Django REST framework 的序列化器如何把对象转换成接口响应。',
            'flow': [
                '视图函数先拿到 Book 模型对象或 QuerySet。',
                'BookSerializer 负责把对象转换成可渲染的 Python 基础类型。',
                'Response 再把这些数据渲染成 JSON 返回给前端。',
            ],
            'endpoints': {
                'book_list': '/api/books/',
                'book_detail': '/api/books/<id>/',
            },
        }
    )


@api_view(['GET'])
def book_list(request):
    seed_demo_books()
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(
        {
            'message': '这里直接返回模型对象列表，不需要手写 json.dumps 或逐个字段拼字典。',
            'count': queryset.count(),
            'results': serializer.data,
        }
    )


@api_view(['GET'])
def book_detail(request, book_id):
    seed_demo_books()
    book = get_object_or_404(Book, id=book_id)
    serializer = BookSerializer(book)
    return Response(
        {
            'message': '单个对象同样交给序列化器处理，视图层只关心拿对象和返回 Response。',
            'result': serializer.data,
        }
    )

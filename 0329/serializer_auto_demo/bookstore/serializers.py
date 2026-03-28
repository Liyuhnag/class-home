from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    display_title = serializers.SerializerMethodField()
    stock_label = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'price',
            'published_date',
            'is_featured',
            'display_title',
            'stock_label',
        ]

    def get_display_title(self, obj):
        return str(obj)

    def get_stock_label(self, obj):
        return '推荐阅读' if obj.is_featured else '普通图书'

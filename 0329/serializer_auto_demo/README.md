# serializer_auto_demo

这个 Django 项目用于演示 Django REST framework 序列化器的核心价值：

- 视图层拿到的是模型对象或 `QuerySet`
- 序列化器负责把对象转换成接口可输出的数据结构
- `Response` 负责把这些数据渲染为 JSON

也就是说，返回对象时不需要自己手动写 `json.dumps()`，也不需要在视图里逐个字段拼字典。

## 运行方式

```bash
cd /Applications/class/0329/serializer_auto_demo
../.venv/bin/python manage.py migrate
../.venv/bin/python manage.py runserver
```

## 访问路径

- `GET /api/`：查看演示说明
- `GET /api/books/`：返回图书列表
- `GET /api/books/1/`：返回单个图书对象

## 关键流程

以 `GET /api/books/` 为例：

1. `book_list` 从数据库取出 `Book.objects.all()`
2. `BookSerializer(queryset, many=True)` 把模型对象转换成基础数据类型
3. `Response(serializer.data)` 输出 JSON

## 示例返回

```json
{
  "message": "这里直接返回模型对象列表，不需要手写 json.dumps 或逐个字段拼字典。",
  "count": 2,
  "results": [
    {
      "id": 1,
      "title": "Django REST Framework 实战",
      "author": "张三",
      "price": "88.00",
      "published_date": "2024-05-01",
      "is_featured": true,
      "display_title": "Django REST Framework 实战 - 张三",
      "stock_label": "推荐阅读"
    }
  ]
}
```

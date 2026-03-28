# MiddlewareMixin 中间件演示

这个项目使用 `django-admin startproject` 创建，专门用于演示自定义中间件继承 `MiddlewareMixin` 时的执行顺序。

## 运行方式

### 单个中间件

```bash
cd middleware_mixin_demo
MIDDLEWARE_DEMO_MODE=single python manage.py runserver
```

访问 `http://127.0.0.1:8000/demo/`，控制台会输出：

```text
[单个中间件] process_request
[单个中间件] process_view
[视图函数] demo_view
[单个中间件] process_response
```

### 多个中间件

```bash
cd middleware_mixin_demo
MIDDLEWARE_DEMO_MODE=multi python manage.py runserver
```

访问 `http://127.0.0.1:8000/demo/`，控制台会输出：

```text
[第一个中间件] process_request
[第二个中间件] process_request
[第一个中间件] process_view
[第二个中间件] process_view
[视图函数] demo_view
[第二个中间件] process_response
[第一个中间件] process_response
```

## Git 提交建议

如果你的环境允许写入 `.git`，建议按下面顺序提交：

1. `使用 django-admin 创建中间件演示项目`
2. `演示单个自定义中间件的执行顺序`
3. `演示多个自定义中间件的执行顺序`

# Django 自定义中间件示例

这个示例在仓库根目录创建了一个独立 Django 项目 `middleware_root_demo`，并在 `middleware_demo` app 中实现了一个继承 `MiddlewareMixin` 的自定义中间件。

## 五个钩子函数

- `process_request`
- `process_view`
- `process_exception`
- `process_template_response`
- `process_response`

## 关键文件

- `manage.py`
- `middleware_root_demo/settings.py`
- `middleware_root_demo/urls.py`
- `middleware_demo/middleware.py`
- `middleware_demo/views.py`
- `middleware_demo/urls.py`
- `middleware_demo/templates/middleware_demo/demo_page.html`

## 演示路由

- `GET /middleware-demo/`
- `GET /middleware-demo/json/`
- `GET /middleware-demo/template/`
- `GET /middleware-demo/exception/`
- `GET /middleware-demo/json/?block=1`

`?block=1` 用于演示 `process_request` 在视图执行前直接返回响应。

## Git 流程

```bash
git status --short
/Applications/class/0329/.venv/bin/django-admin startproject middleware_root_demo .
/Applications/class/0329/.venv/bin/python manage.py startapp middleware_demo
git status --short
git add manage.py middleware_root_demo middleware_demo MIDDLEWARE_DEMO.md
git diff --cached
```

## 运行

```bash
/Applications/class/0329/.venv/bin/python manage.py runserver
```

## 测试

```bash
/Applications/class/0329/.venv/bin/python manage.py test middleware_demo
```

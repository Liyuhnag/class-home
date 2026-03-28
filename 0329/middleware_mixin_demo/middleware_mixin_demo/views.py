from django.http import HttpResponse


def demo_view(request):
    print("[视图函数] demo_view")
    return HttpResponse("MiddlewareMixin 中间件执行顺序演示")

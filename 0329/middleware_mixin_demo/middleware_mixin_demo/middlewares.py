from django.utils.deprecation import MiddlewareMixin


class SingleTraceMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("[单个中间件] process_request")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("[单个中间件] process_view")

    def process_response(self, request, response):
        print("[单个中间件] process_response")
        return response


class FirstTraceMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("[第一个中间件] process_request")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("[第一个中间件] process_view")

    def process_response(self, request, response):
        print("[第一个中间件] process_response")
        return response


class SecondTraceMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("[第二个中间件] process_request")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("[第二个中间件] process_view")

    def process_response(self, request, response):
        print("[第二个中间件] process_response")
        return response

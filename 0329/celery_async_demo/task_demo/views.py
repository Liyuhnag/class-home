from django.shortcuts import render

# Create your views here.
import time

from django.http import JsonResponse


def sleep_test_view(request):
    started_at = time.time()
    time.sleep(3)
    finished_at = time.time()
    return JsonResponse(
        {
            "message": "这是一个用于演示阻塞效果的测试接口。",
            "mode": "sleep-test",
            "duration_seconds": round(finished_at - started_at, 2),
        }
    )

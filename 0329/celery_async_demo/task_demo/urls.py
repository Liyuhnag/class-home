from django.urls import path

from .views import sleep_test_view

urlpatterns = [
    path("sleep-test/", sleep_test_view, name="sleep-test"),
]

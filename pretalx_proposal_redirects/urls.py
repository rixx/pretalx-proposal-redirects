from django.urls import path

from .views import redirect_view

urlpatterns = [
    path("<str:code>", redirect_view, name="redirect"),
]

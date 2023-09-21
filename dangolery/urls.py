from django.urls import path

from dangolery.views import index

urlpatterns = [
    path("", index, name="index"),
]

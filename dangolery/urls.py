from django.urls import path

from dangolery.views import add, index

urlpatterns = [
    path("", index, name="index"),
    path("add/", add, name="add"),
]

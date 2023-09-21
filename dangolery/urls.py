from django.urls import path

from dangolery.views import add, index, view

urlpatterns = [
    path("", index, name="index"),
    path("add/", add, name="add"),
    path("view/", view, name="view"),
]

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "dangolery/index.html")


def add(request):
    return render(request, "dangolery/add.html")

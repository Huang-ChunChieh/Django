import imp
from multiprocessing import context
from django.shortcuts import render


def index(request):
    context = {}
    context["name"] = "HuangChieh"
    return render(request, "index.html", context)

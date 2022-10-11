from django.shortcuts import render
from django.http import HttpResponse  # import 需要的套件

# Create your views here.


def index(request):
    return HttpResponse("Hello World")
# 建立名為index的方法，回應訪問者的request，會回傳Hello World!到訪問者端(也就是顯示在訪問者開啟的網頁上)

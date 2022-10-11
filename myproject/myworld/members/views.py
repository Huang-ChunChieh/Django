#from re import template
#from unittest import loader#
#from django.shortcuts import render
from django.http import HttpResponse  # import 需要的套件
from django.template import loader  # 用來載入template的套件
from .models import Members  # 把Members這張資料表 import 進來

# Create your views here.


def index(request):
    mymembers = Members.objects.all().values()
    # 建立變數mymembers存放Members上的所有紀錄，這些紀錄會被包在一個List裡面被回傳
    output = ""  # output
    for x in mymembers:  # 使用For迴圈逐一將Members上每筆紀錄的firstname欄位值和output串接在一起
        output += x["firstname"]
    return HttpResponse(output)  # 將這些字串回傳到瀏覽器並顯示在畫面上

from django.http import HttpResponse
from django.shortcuts import render  # import 需要的套件
from django.template import loader  # 用來載入template的套件
from .models import Members  # 把Members這張資料表 import 進來

# Create your views here.


def index(request):
    mymembers = Members.objects.all().values()
    # 1.將Members資料表的紀錄(Reoord)取出來放到mymembers裡面
    template = loader.get_template('index.html')
    # 2.載入index.html這個Template並放到同名變數template裡面
    context = {
        'mymembers': mymembers,
    }  # 3.建立名為context的變數，然後以Dict的Key-Value形式，放進變數mymembers
    return HttpResponse(template.render(context, request))
    # 4.把攜帶著資料表紀錄資料的context傳到template裡面，最後以template回應請求並顯示在瀏覽器的視窗畫面上


def add(request):
    template = loader.get_template('add.html')  # 1.載入製作好的表單(Template)
    return HttpResponse(template.render({}, request))
    # 2.把表單回應傳送到訪問者的瀏覽器並顯示出來，因為不需要送資料到表單，所以在方法內傳入{}(空的context)。


def home(request):
    return render(request, "home.html")  # 回傳template


def day_ten(request):
    return render(request, "day10.html")  # 回傳template


def day_eleven(request):
    return render(request, "day11.html")  # 回傳template

from django.http import HttpResponse, HttpResponseRedirect
# HttpResponseRedirect是HttpResponse的subclass，用來做路徑的重新導向
from django.shortcuts import render  # import 需要的套件
from django.template import loader  # 用來載入template的套件
from .models import Members  # 把Members這張資料表 import 進來
from django.urls import reverse
# reverse的功能是允許使用前面說過的path別名，來找到對應的路徑和相應的view方法

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


def addrecord(request):
    x = request.POST['first']
    # 1.表單是以POST的方式將資料含在HttpRequest裡寄出，因此需要找HttpRequest物件(request)的POST屬性拿資料。
    # 從POST這個屬性拿到的資料，它本身會是個QueryDict，也就是Python裡為人熟知的Key-Value結構。
    # 因此會用POST['first']的形式去拿到表單name=first的資料值。
    y = request.POST['last']  # 2.同理，用POST['last']的形式去拿到表單name=last的資料值。
    member = Members(firstname=x, lastname=y)
    # 3.把拿到的資料值用來建立Members物件即要新增到資料表的新紀錄(Record)並以變數member承接
    member.save()  # 4.實際將這筆新的紀錄(Record)存放到資料表上
    return HttpResponseRedirect(reverse('index'))
    # 5.HttpResponseRedirect用來重新導引路徑
    # reverse('index')可以把它想成path('', views.index, name='index')，也就是新增完資料後跳轉回members/


def home(request):
    return render(request, "home.html")  # 回傳template


def day_ten(request):
    return render(request, "day10.html")  # 回傳template


def day_eleven(request):
    return render(request, "day11.html")  # 回傳template

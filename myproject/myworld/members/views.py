from re import template
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


def delete(request, id):
    # 1.在URLs的部分有說過delete會以delete(request,id)的格式被呼叫，所以這邊才會如此定義該方法
    member = Members.objects.get(id=id)
    # 2.Members.objects.get(id=id)被定義在QuerySet下的方法，用來在資料表中尋找符合特定欄位值的紀錄(Record)，這邊在資料表上尋找id相同於點擊刪除資料那列id的紀錄
    member.delete()
    # 3.Django的資料庫操作採用的是ORM，所以這邊可以直接使用映射物件自帶的delete方法去刪除資料表上的紀錄(Record)
    return HttpResponseRedirect(reverse('index'))
    # 4.刪除資料後跳轉回原先呈現表格資料的index.html頁面


def update(request, id):  # 1. members/urls.py使用帶有參數的path，所以方法update的參數包含request和id。
    mymember = Members.objects.get(id=id)
    # 2. 把特定id的資料表紀錄(Record)拿出來放到mymember裡面。
    template = loader.get_template('update.html')
    # 3. 載入update.html為要顯示在瀏覽器畫面的template
    context = {  # 4. context採key-value的形式，它是要傳入template(update.html) 的資料，這裡把剛剛拿到的資料表紀錄放進去。
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
    # 5. 將資料(context)傳入template(update.html)，然後把網頁渲染到瀏覽器的畫面上。


def updaterecord(request, id):
    # 1.path本身帶有參數的關係，所以在urls.py裡面，updaterecord方法實際會以updaterecord(request,id)的形式被呼叫。
    first = request.POST['first']
    # 2. 送出表單所產生的HttpRequest(即request)物件的POST屬性取得資料值，
    #    POST它是Key-Value的形式，這也是為什麼這邊要用request.POST['first']的形式去取得表單上name=first那欄的資料。
    last = request.POST['last']  # 3. 同上，取得表單上name=last那欄的資料
    member = Members.objects.get(id=id)
    # 4. 以獨一無二的id值將要更新的資料表資料(Record)抓出來。
    member.firstname = first
    # 5. 使用類似物件導向的方式指定資料的firstname欄位要更新的值(即first)。
    member.lastname = last
    # 6. 使用類似物件導向的方式指定資料的lastname欄位要更新的值(即last)。
    member.save()
    # 7. 將這次對資料(Record)的修改存到資料表，也就是更新資料表資料。
    return HttpResponseRedirect(reverse('index'))
    # 8. 透過reverse('index')找到別名為index的path，再藉著HttpResponseRedirect將頁面重新導向指定路徑(即最初的資料表格頁面)。


def testing_day20(request):
    template = loader.get_template('testing_day20.html')
    return HttpResponse(template.render())


def testing_day21n22(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('testing_day21n22.html')
    context = {
        'mymembers': mymembers,
        'emptyObject': [],  # 後面測試For迴圈會用到就順便傳到前端網頁
    }
    return HttpResponse(template.render(context, request))


def home(request):
    return render(request, "home.html")  # 回傳template


def day_ten(request):
    return render(request, "day10.html")  # 回傳template


def day_eleven(request):
    return render(request, "day11.html")  # 回傳template


def day_sixteen(request):
    return render(request, "day16.html")  # 回傳template

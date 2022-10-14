from django.urls import path
from . import views

#urlpatterns: list裡面放的是members這個App下面所有網頁的路徑
urlpatterns = [
    path('', views.home, name='home'),
    path("index/add/", views.add, name='add'),
    # 新增到members/add的路徑，當收到訪問者訪問該路徑的請求則以views.py的add方法處理和回應。
    # 若有必要在views或templates使用到這個路徑，則可用add代稱。
    path('index/add/addrecord/', views.addrecord, name='addrecord'),
    # 設定到index/add/addrecord的路徑，以members/views.py的addrecord處理請求並給定路徑別名addrecord
    path('index/delete/<int:id>', views.delete, name='delete'),
    # 新格式<int:id>是用來讓path可以攜帶參數，int是參數型別，id是參數名稱。
    # 除新格式外，views.py的delete方法在處理請求時也跟前面不同，delete方法會以delete(request,id)的形式被呼叫，而最後的路徑別名則是跟之前相同沒有改變功能。
    path('index/', views.index, name='index'),
    path('day10/', views.day_ten, name='day_ten'),
    path('day11/', views.day_eleven, name='day_eleven'),
    path('day16/', views.day_sixteen, name='day_sixteen'),
]
# '' : 相當於設定路經為xxx/members/，xxx會是什麼與你使用的Server有關，如果用的是localhost，那基本上會是127.0.0.1:8000/members/
# views.index : 收到來自127.0.0.1:8000/members/的request，以members/views.py的index方法回應
# name='index' : 設定path的別名。這邊取別名是有理由的，如果在views或templates需要用到這個路徑，就可以不用寫完整路徑而使用別名代稱。

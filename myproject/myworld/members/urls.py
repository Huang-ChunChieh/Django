from django.urls import path
from . import views

#urlpatterns: list裡面放的是members這個App下面所有網頁的路徑
urlpatterns = [
    path('', views.index, name='index')
]
# '' : 相當於設定路經為xxx/members/，xxx會是什麼與你使用的Server有關，如果用的是localhost，那基本上會是127.0.0.1:8000/members/
# views.index : 收到來自127.0.0.1:8000/members/的request，以members/views.py的index方法回應
# name='index' : 設定path的別名。這邊取別名是有理由的，如果在views或templates需要用到這個路徑，就可以不用寫完整路徑而使用別名代稱。

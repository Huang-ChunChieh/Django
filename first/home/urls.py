from django.urls import path
from .import views

urlpatterns = [
    path('', views.simple_crawl),
    path('POST_crawl/', views.POST_crawl),
]

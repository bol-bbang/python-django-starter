from django.urls import path
from . import views

'''views.post_list 는 views 파일안에 있는 post_list라는 함수'''
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
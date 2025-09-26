# todo/urls.py
from django.urls import path
from . import views

# URL을 뷰와 연결
urlpatterns = [
    # p82 기본 url에서 to_list함수형 뷰로 연결
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
]
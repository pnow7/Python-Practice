# todo/urls.py
from django.urls import path
from . import views

# URL을 뷰와 연결
urlpatterns = [
    # p82 기본 url에서 to_list함수형 뷰로 연결
    path('', views.todo_list, name='todo_list'),

    # p85 상세조회
    path('<int:pk>/', views.todo_detail, name='todo_detail'),

    # 88p 등록*127.0.0.1/todo/post/
    path('post/', views.todo_post, name='todo_post'),

    # p89 Todo 수정 URL 연결하기
    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    
    # p92 Todo 완료 URL 연결하기
    path('done/', views.done_list, name='done_list'),
    path('done/<int:pk>/', views.todo_done, name='todo_done'),
]
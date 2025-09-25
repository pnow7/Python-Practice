## photo/urls.py 생성

from django.urls import path
from . import views

## p.58 
urlpatterns = [
    # localhost:8000/ 은 photo/views.py에서 photo_list함수에 지정된 곳으로 연결됨
    path('', views.photo_list, name='photo_list'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),

    # 등록: photo_post라는 이름으로 views로 전달
    path('photo/new/', views.photo_post, name='photo_post'),

    # 수정: photo_detail.html에서 아래의 name='photo_edit'에 지정된 링크를 가져가서 html에 삽입
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),

    # 삭제
    path('photo/<int:pk>/remove/', views.photo_remove, name='photo_remove')
]
from django.contrib import admin
from .models import Todo

# p79 Todo 모델을 관리자 페이지에 등록
admin.site.register(Todo)
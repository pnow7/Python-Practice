# todo/forms.py
# p85 Todo 생성 템플릿 만들기 (새로 생성한 파일)
from django import forms
from .models import Todo


# 같은 앱(todo)의 models.py에서 Todo 모델을 가져옴
# 이 모델을 기반으로 자동으로 폼을 생성
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo

        # 모델의 모든 필드를 쓰지 않고,
        # title, description, important 세 가지만 사용자 입력 가능하도록 설정
        fields = ['title', 'description', 'important']
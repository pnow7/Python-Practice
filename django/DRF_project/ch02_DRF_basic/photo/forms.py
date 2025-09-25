from django import forms
from .models import Photo

# Form에서 입력받을 Photo DB의 필드 설정(컬럼들)
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'title',
            'author',
            'image',
            'description',
            'price',
        ]
from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo': photo})

# 등록
# urls.py로 부터 받은 photo_post -> views.photo_post로 연결됨
def photo_post(request):
    if request.method == "POST":
        # 사용자가 보낸 데이터로 폼 생성
        form = PhotoForm(request.POST)
        if form.is_valid():
            # DB에 바로 저장하지 않고 Photo 객체 생성
            photo = form.save(commit=False)
            # DB에 최종 저장
            photo.save()
            # 저장 후 상세 페이지로 리다이렉트
            # 저장된 객체의 기본키(Primary Key)를 URL 파라미터로 전달
            return redirect('photo_detail', pk=photo.pk)
    # POST 요청이 아니라면(GET 요청이면) 빈 폼 생성    
    else:
        form = PhotoForm()
    # GET 요청이거나, POST 요청이지만 FOrm이 유효하지 않을 때
    # 다시 같은 템플릿을 보여주면서 오류 메세지와 함께 기존 입력값을 그대로 출력
    return render(request, 'photo/photo_post.html', {'form': form})

# 수정
def photo_edit(request, pk):
    # pk에 해당하는 Photo 객체 가져오기 (없으면 404 반환)
    photo = get_object_or_404(Photo, pk=pk)

    if request.method == 'POST':  # 수정 폼 제출한 경우
        # 기존 photo 객체에 POST 데이터 바인딩
        form = PhotoForm(request.POST, request.FILES, instance=photo)

        if form.is_valid():  # 유효성 검사 통과 시
            photo = form.save(commit=False)  # DB 저장 전 객체 생성 (수정 가능하도록)
            # photo.updated_at = timezone.now()  # 필요하면 수정 시간 기록 가능
            photo.save()  # DB에 최종 저장
            return redirect('photo_detail', pk=photo.pk)  # 상세 페이지로 이동
    # GET 요청 시 (수정 페이지 처음 열 때)
    else: 
        # 기존 값이 채워진 Form 생성
        form = PhotoForm(instance=photo)  

    # 새 글 작성 템플릿을 재활용하여 수정 화면 렌더링
    return render(request, 'photo/photo_post.html', {'form': form})

# 삭제
def photo_remove(request, pk):
    # 삭제하려는 사진 객체를 가져옴
    photo = get_object_or_404(Photo, pk=pk)
    
    # HTTP 요청이 POST 방식인지 확인
    # 일반적으로 삭제는 POST 방식으로 처리하는 것이 안전
    if request.method == "POST":
        # photo 객체를 데이터베이스에서 삭제
        photo.delete()  
        # 삭제 후 사진 목록 페이지로 리다이렉트
        return redirect('photo_list')  
    
    # POST 방식이 아닐 경우(GET 방식)에는 삭제 확인 페이지를 보여줌
    # 사용자가 삭제 버튼을 누르기 전에 "정말 삭제하시겠습니까?" 와 같은 메시지를 보여주는 것이 좋음
    return render(request, 'photo/photo_confirm_delete.html', {'photo': photo})
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# p82 Todo 전체 조회 뷰(함수뷰) 만들기
def todo_list(request):
    # DB에서 complete=False인 할 일만 가져옴 → 즉, 아직 끝나지 않은 할 일 목록
    todos = Todo.objects.filter(complete=False)
    # todos = Todo.objects.all()  # 전체 조회할 때

    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

# p87 Todo 생성 뷰 만들기
def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            # db에 저장
            todo.save()
            # urls.py에 name='to_list'인 url로 이동
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form': form})

# p88 Todo 수정 뷰 만들기
def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)  # Todo DB에서 id=pk인 데이터 읽어옴
    if request.method == "POST":    # 사용자가 화면에서 폼을 제출했을 때
        # 기존 todo 객체를 instance로 넣어서, 새로운 값으로 업데이트하도록 설정
        form = TodoForm(request.POST, instance=todo)  # 생성이 아니라 수정
        if form.is_valid():  # 모델의 제약조건(유효성 검사)을 통과했는지 확인
            todo = form.save(commit=False)  # DB에는 아직 저장하지 않고 Todo 객체만 반환
            todo.save()                     # 최종적으로 DB에 저장

            # 수정이 완료되면 다시 전체 목록 페이지(todo_list 뷰)로 이동
            return redirect('todo_list')
    else:   # GET 요청 시
        # 기존 todo 객체의 값을 가진 폼을 생성해서 사용자에게 보여줌
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form': form})

# 완료된 Todo 목록을 보여주는 뷰  (todo_list.html에서 "완료한 TODO 목록" 클릭시 실행)
def done_list(request):
    # DB에서 complete=True 인 Todo 객체만 조회
    dones = Todo.objects.filter(complete=True)
    # 조회된 객체들을 'done_list.html' 템플릿에 전달
    return render(request, 'todo/done_list.html', {'dones': dones})


# 특정 Todo 항목을 '완료' 상태로 변경하는 뷰 (todo_list.html에서 "완료"버튼 눌렀을 때 실행)
def todo_done(request, pk):
    # pk(primary key, id)에 해당하는 Todo 객체를 DB에서 가져오기
    todo = Todo.objects.get(id=pk)
    todo.complete = True  # 해당 Todo의 complete 필드를 True로 변경 (완료 처리)
    print("~~~~~~~~ todo.complete=", todo.complete)
    todo.save()  # 변경 사항 DB에 저장

    # 완료 처리 후 다시 Todo 목록 페이지로 리다이렉트
    return redirect('todo_list')
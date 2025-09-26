from django.shortcuts import render, redirect
from .models import Todo


# p82 Todo 전체 조회 뷰(함수뷰) 만들기
def todo_list(request):
    # DB에서 complete=False인 할 일만 가져옴 → 즉, 아직 끝나지 않은 할 일 목록
    todos = Todo.objects.filter(complete=False)
    # todos = Todo.objects.all()  # 전체 조회할 때

    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})
from django.shortcuts import render


def loadTodoPage(request):
    return render(request, 'todo.html')

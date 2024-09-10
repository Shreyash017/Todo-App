from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.
def home(request):
    return render(request, 'index.html')


def todoList(request):
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            
            # Validation: Title and description are required
            if not title or not description:
                return render(request, 'todos.html', {
                    "css_file" : "todos",
                    'todos': Todo.objects.all(),
                    'error': 'Title and Description are required.'
                }, status=400)
            
            # Validation: Title and description must be strings
            if not isinstance(title, str) or not isinstance(description, str):
                todos = Todo.objects.all()
                return render(request, 'todos.html', {
                    "css_file" : "todos",
                    'todos': todos, 
                    'error': 'Title and Description must be strings.'
                    }, status=400)
            
            todo = Todo(title=title, description=description)
            todo.save()
            return redirect('todoList')
    except Exception as e:
        print("Error: ", e)
    
    todos = Todo.objects.all()
    return render(request, 'todos.html', {"css_file" : "todos", 'todos': todos})


def todoUpdate(request, pk):
    try:
        todo = get_object_or_404(Todo, pk=pk)
        if request.method == 'POST':
            todo.title = request.POST.get('title')
            todo.description = request.POST.get('description')
            todo.completed = request.POST.get('completed') == 'on'
            
            # Validation: Title and description are required
            if not todo.title or not todo.description:
                return render(request, 'todo_update.html', {
                    "css_file" : "update",
                    'todo': todo,
                    'error': 'Title and Description are required.'
                }, status=400)
            
            # Validation: Title and description must be strings
            if not isinstance(todo.title, str) or not isinstance(todo.description, str):
                return render(request, 'todo_update.html', {
                    "css_file" : "update",
                    'todo': todo, 
                    'error': 'Title and Description must be strings.'
                    }, status=400)
            
            todo.save()
            return redirect('todoList')
        
        return render(request, 'todo_update.html', {"css_file" : "update", 'todo': todo})
    except Exception as e:
        print("Error: ", e)
        
    return redirect('todoList')


def todoDelete(request, pk):
    try:
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
    except Exception as e:
        print("Error: ", e)
    return redirect('todoList')

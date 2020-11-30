from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm


# Create your views here.
def view_todo(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todo/index.html', context)


def add_todo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'todo/index.html', context)


def completed_todo(request):
    return None

def update_todo(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=todo)
    context = {'form': form}
    return render(request, 'todo/update.html', context)


def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        # I know I don't have to do this but there are one off instances
        # where checking is good
        # Some instances where for example the admin already deleted it, rather than
        # displaying an error, checking if it exists and if not, just sending them
        # to the main page
        todo.delete()
        return redirect('index')
    context = {'todo': todo}
    return render(request, 'todo/delete.html', context)

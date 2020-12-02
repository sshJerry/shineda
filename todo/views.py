from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm


# Create your views here.
def view_todo(request,):
    form_add = TaskForm()

    if request.method == 'POST':
        form_add = TaskForm(request.POST)
        if form_add.is_valid():
            form_add.save()
            return redirect('index')
    todos = Todo.objects.all()
    context = {'todos': todos, 'form_add': form_add}
    return render(request, 'todo/index.html', context)


def completed_todo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.__setattr__(True)
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=todo)
    context = {'form': form}
    return render(request, 'todo/index.html', context)


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
        todo.delete()
        return redirect('index')
    context = {'todo': todo}
    return render(request, 'todo/delete.html', context)

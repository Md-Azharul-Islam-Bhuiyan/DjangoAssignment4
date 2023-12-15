from django.shortcuts import render, redirect
from task.forms import TaskForm
from task.models import TaskModel

def add_task(request):
    if request.method == 'POST':
       task_from = TaskForm(request.POST)
       if task_from.is_valid():
           task_from.save()
           return redirect('showTask')
        #    print(task_from.cleaned_data)
    else:
        task_from = TaskForm()
    return render(request, 'add_task.html', {'form': task_from})

def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task_from = TaskForm(instance=task)
    if request.method == 'POST':
       task_from = TaskForm(request.POST, instance=task)
       if task_from.is_valid():
           task_from.save()
           return redirect('showTask')
        #    print(task_from.cleaned_data)

    return render(request, 'add_task.html', {'form': task_from})

def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('showTask')
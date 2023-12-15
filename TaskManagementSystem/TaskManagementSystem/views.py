from django.shortcuts import render
from task.models import TaskModel

def showTask(request):
    data = TaskModel.objects.all()
    return render(request, 'showTask.html', {'data': data})
from django.shortcuts import render
from task.models import taskModel


def show(request):
    tasks = taskModel.objects.all()
    return render(request,'show.html',{'tasks':tasks})

def home(request):
    return render(request,'home.html')
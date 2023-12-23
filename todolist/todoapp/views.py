from django.shortcuts import render
from . models import Task
# from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {'success' : False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        details = Task(taskTitle=title,taskdesc=desc)
        details.save()
        context = {'success' : True}
    
    return render(request,'home.html',context)

def task(request):
    alltasks = Task.objects.all()
    content = {'tasks' : alltasks}
    return render(request,'task.html',content)

def edit_task(request):
    return render(request,'edit.html')
from django.shortcuts import render, redirect
from . models import Task

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

def delete(request):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task')
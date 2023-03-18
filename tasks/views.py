from django.shortcuts import render, redirect
from .models import Task 
# Create your views here.
def list_tasks (request):
    tasks=Task.objects.all()
    return render (request,'list_tasks.html',{'tasks':tasks})

def create_task (request):
    task= Task(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'],
               precio=request.POST['precio'], cantidad=request.POST['cantidad'],
               categoria=request.POST['categoria'] )
    task.save()
    return redirect('/tasks/')

def delete_task (request,task_codigo):
    task=Task.objects.get(codigo=task_codigo)
    task.delete()
    return redirect('/tasks/')

def update_task(request, task_codigo):
    task = Task.objects.get(codigo=task_codigo)
    if request.method == 'POST':
        task.nombre = request.POST['nombre']
        task.descripcion = request.POST['descripcion']
        task.precio = request.POST['precio']
        task.cantidad = request.POST['cantidad']
        task.categoria = request.POST['categoria']
        task.save()
        return redirect('/tasks/')
    else:
        return render(request, 'update_task.html', {'task': task})

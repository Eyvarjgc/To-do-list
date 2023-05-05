from django.shortcuts import render,redirect
from django.http import request
from .models import days,task,Messages
from .form import UserRegistration,AddTask,AddTask2
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.models import User
# Create your views here.

# HOME
def Home(request):
    coments = Messages.objects.all()

    querry = request.GET.get('buscar')

    if querry:
        querry = task.objects.filter(
            Q(name__icontains = querry)|
            Q(day__name__icontains = querry)
        )
    else:
        querry = task.objects.all()
    day = days.objects.all()
    # tasks = task.objects.all()

    listcount = querry.count()

    context = {
        'listcount':listcount,
        'comment':coments,
        'dias':day,
        'tasks':querry
    }
    return render(request,'app/home.html',context)


# VISTA DE TAREAS
def TaskView(request,pk):
        day = days.objects.all()
        Tasks = task.objects.filter(day_id = pk)
        listcount = Tasks.count()
        # if request.method == 'POST':
        #     if request.POST.get('save'):
        #         for item in Tasks:
        #             print(item)
        #             if request.POST.get('c' + str(item.id)) == 'clicked':
        #                 print("True")
        #                 item.checkout = True
        #             else:
        #                 print("False")
        #                 item.checkout = False
        #         return redirect('home')
        if request.method == 'POST':    
            pass



        context={
            'listcount':listcount,
            'tasks':Tasks,
            'dias':day,
        }
        return render(request,'app/task.html',context)


# VISTA DE REGISTRO
def Register(request):
        form = UserRegistration()
        if request.method == 'POST':
            form = UserRegistration(request.POST)
            if form.is_valid:
                user = form.save()
                user.username = user.username.lower()
                user.save()
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'No ha ingresado la contraseña correctamente')
        return render(request,'app/register.html',{'form':form})


# VISTA AÑADIR TAREAS
@login_required
def addtask(request):
    day = days.objects.all()
    form = AddTask(request.POST or None)
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context={
        'form':form,
        'dias':day,
    }
    return render(request,'app/addtask.html',context)
    


# LOGOUT USER
def logoutUser(request):
    logout(request)
    return redirect('home')


# VISTA ELIMINAR TAREA
@login_required
def delete(request,id):
        day = days.objects.all()
        taskk = task.objects.get(id = id)
        if request.method == 'POST':
            taskk.delete()
            return redirect('home')
        return render(request,'app/delete.html',{'taskk':taskk,'dias':day})


# LOGIN
def Login(request):
    # usuario = User
    # context = {
    #     'user':User
    # }
    return render(request,'registration/login.html')


# VISTA COMENTARIOS
def coments(request,id):
    day = days.objects.all()
    tasks = task.objects.get(id=id)
    comment = tasks.messages_set.all()
    if request.method == 'POST':
        message = Messages.objects.create(
            user = request.user,
            task = tasks,
            body = request.POST.get('body')
        ) 
        return redirect('coments', id=tasks.id)
    
    context = {
        'tasks':tasks,
        'comment':comment,
        'dias':day
    }
    
    return render(request,'app/coments.html',context)


# VISTA EDITAR NOMBRE
@login_required
def edit(request,id):
    day = days.objects.all()
    tasks = task.objects.get(id = id)
    # edittask = AddTask(instance = tasks)
    if request.method == 'POST':
    #     edittask = AddTask2(instance = tasks)
    #     if edittask.is_valid():
        tasks.name = request.POST.get('name')
        tasks.save()
        return redirect('home')
    context = {
        'dias':day,
        'task':tasks
    }
    return render(request,'app/edit.html',context)











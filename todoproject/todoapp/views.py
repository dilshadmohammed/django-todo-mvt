from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = Todo(user=request.user,task=task)
        new_todo.save()

    all_todos = Todo.objects.filter(user=request.user)
    return render(request, 'todoapp/todo.html',{'todos':all_todos})

def filter(request, flag='all'):
    if flag == 'completed':
        todos = Todo.objects.filter(user=request.user, completed=True)
    elif flag == 'expired':
        todos = Todo.objects.filter(user=request.user, expiry__lt=timezone.now(), completed=False)
    elif flag == 'active':
        todos = Todo.objects.filter(user=request.user, expiry__gt=timezone.now(), completed=False)
    else:
        todos = Todo.objects.filter(user=request.user)

    return render(request, 'todoapp/todo.html', {'todos': todos})
        

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cfpass')
        
        if confirm_password != password:
            messages.error(request,'Passwords not matched')
            return redirect('register')

        if len(password) < 5:
            messages.error(request, 'Password must be at least 5 characters')
            return redirect('register')

        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request, 'Error, username already exists try different name.')
            return redirect('register')

        new_user = User.objects.create_user(username=username,password=password)
        new_user.save()

        messages.success(request,'User successfully created, login now')
        return redirect('login')
    return render(request, 'todoapp/register.html', {})

def LogoutView(request):
    logout(request)
    return redirect('login')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')


    return render(request, 'todoapp/login.html', {})

@login_required
def DeleteTask(request, id):
    item = Todo.objects.get(user=request.user, id=id)
    item.delete()
    return redirect('home-page')

@login_required
def Update(request, id):
    item = Todo.objects.get(user=request.user, id=id)
    item.completed = True
    item.save()
    return redirect('home-page')
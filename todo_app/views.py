from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import List, Task

# Create your views here.

def home(request): 
    return render(request, "home.html")    

def signup(request):                                                   
    if request.method == "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]

        if password==password2:
            if User.objects.filter(username=username).exists():
                return redirect("/signup")
            elif User.objects.filter(email=email).exists():
                return redirect("/signup")
            else:
                new_user=User.objects.create_user(username=username, email=email, password=password)
                new_user.save()
                #user_login=auth.authenticate(username=username, password=password)
                #auth.login(request,user_login)
                return redirect("/signin")
        else:
            return redirect("/signup")
    else:
        return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return redirect("/signin")    
    else:
        return render(request, "signin.html")
    
@login_required(login_url='signin')      
def logout(request):
    auth.logout(request)
    return redirect("/signin")

@login_required(login_url='signin')
def lists(request):
    user = request.user 
    lists = List.objects.filter(user=user)
    return render(request, "list.html", {"lists":lists})

@login_required(login_url='signin')
def tasks(request, id):
    list = List.objects.get(id=id)
    tasks = Task.objects.filter(list=list)
    return render(request, "task.html", {"tasks":tasks, "list_name":list.name, "list_id":list.id})

@login_required(login_url='signin')
def is_done(request, id):
    task = Task.objects.get(id=id)
    list_id = task.list.id
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()    
    return redirect(f"/todo/{str(list_id)}")            

@login_required(login_url='signin')
def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    list_id = task.list.id
    return redirect(f"/todo/{str(list_id)}")

@login_required(login_url='signin')
def add_task(request,id):
    task_description = request.POST["description"]
    list = List.objects.get(id=int(id))
    task = Task.objects.create(list=list, description=task_description)
    task.save()
    return redirect(f"/todo/{id}")
    
@login_required(login_url='signin')    
def add_list(request):
    name = request.POST["name"]
    user = request.user
    list = List.objects.create(name=name, user=user) 
    list.save()
    return redirect("/lists") 


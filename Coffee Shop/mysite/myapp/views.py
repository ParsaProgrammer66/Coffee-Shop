from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import SignupForm,LoginForm,UserEdit,DeleteForm
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'myapp/index.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            user=User.objects.create_user(cd['username'],cd['email'],cd['password'])
            if cd['password'] == cd['password2']:
                user.save()
                return redirect('login')
            else:
                return HttpResponse("<div style='color:red'>your password didnt match</div>")
    else:
        form=SignupForm()

    return render(request,'myapp/signup.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse('invalid')
    else:
        form=LoginForm()
    
    return render(request,'myapp/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return render(request,'myapp/logout.html')

@login_required
def edit_profile(request):
    if request.method=='POST':
        user_form=UserEdit(instance=request.user,data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('index')
    else:
        user_form=UserEdit(instance=request.user)
    return render(request,'myapp/edit_profile.html',{'user_form':user_form})

@login_required
def delete_user(request):
    if request.method=='POST':
        user=request.user.delete()
        return redirect('index')
    else:
        form=DeleteForm(instance=request.user)
        return render(request,'myapp/delete.html')
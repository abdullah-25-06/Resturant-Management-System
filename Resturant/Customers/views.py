from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate ,login,logout
from django.urls import reverse
from .form import UserCreationForm
from django.contrib import messages
from django.contrib.auth import get_user_model
# Create your views here.


    
def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('canteen:index'))
    else:
        if request.method == 'POST':
            form = UserCreationForm(request=request, data=request.POST)
            if form.is_valid():
                # form.save()
                form.save()
                username = form.cleaned_data['username']
                password1 = form.cleaned_data['password1']
                user = authenticate(request,username=username, password=password1)
                login(request,user)
                return HttpResponseRedirect(reverse('canteen:index'))
        else:
            form = UserCreationForm(request=request)
        context={
            'form': form,
            'pg_name':'reg'
            }
        return render(request, 'Customers/regform.html', context)

def login1(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('canteen:index'))
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        if user is not None:
            login(request, user)
            
            return HttpResponseRedirect(reverse('canteen:index'))
        else:
            messages.error(request, "Username and Password doesn't exist")
            return render(request,'Customers/regform.html')        
    return render(request,'Customers/regform.html')

def logout1(request):
    logout(request)
    return HttpResponseRedirect(reverse('canteen:index'))
from django.shortcuts import render, redirect
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

def register(response):
    if response.method=="POST":
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            '''
            Needs fixing -- not redirecting to the right page 
            '''
        return redirect('/')
    else:
        form=RegisterForm()
    return render(response, 'userApp/signup.html', {'form':form})

from django.shortcuts import render, redirect
from .models import User, Student
from django.contrib import messages
import bcrypt

def index(request):
    #!!!!!!!!!!!!!!!!!!!!
    # Render page left blank until Denys names login page
    #!!!!!!!!!!!!!!!!!!!!

    return render(request, '')

def register(request):

    # Register Validator
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    # Register functionality
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(
                        name = request.POST['parent_name'],
                        email = request.POST['email'],
                        password = pw_hash

    )
    user = User.objects.last()
    request.session['user_id'] = user.id
    #!!!!!!!!!!!!!!!!!!!!
    # Redirect left blank until Denys names homepage
    #!!!!!!!!!!!!!!!!!!!!
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    user = User.objects.get(email=request.POST['email'])
    if user:
        request.session['user_id'] = user.id
        #!!!!!!!!!!!!!!!!!!!!
        # Redirect left blank until Denys names homepage
        #!!!!!!!!!!!!!!!!!!!!
        return redirect('/')

    return redirect('/')
    

def logout(request):
    del request.session['user_id']
    return redirect('/')

    
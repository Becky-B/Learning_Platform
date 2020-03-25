from django.shortcuts import render, redirect
from login.models import User, Student
from django.contrib import messages

def add_student(request, user_id):
    user = User.objects.get(id=request.session['user_id'])
    Student.objects.create(
                            name = request.POST['name'],
                            user = user,
                            grade = request.POST['grade']
    )
    # !!!!!!!!!!!!!!!!!!!!!!
    # Redirect blank
    # !!!!!!!!!!!!!!!!!!!!!!!
    return redirect('/')

def st_patty(request):
    errors = User.objects.st_patty_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
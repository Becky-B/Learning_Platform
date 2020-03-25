from django.shortcuts import render, redirect
from login.models import User, Student, Reading
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
    errors = Reading.objects.st_patty(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect back to short1.html
        return redirect('/')
        # redirect to Good job page.
    return redirect('/')

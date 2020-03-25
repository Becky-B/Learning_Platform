from django.shortcuts import render, redirect
from login.models import User, Student

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
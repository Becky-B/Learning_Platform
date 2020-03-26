from django.shortcuts import render, redirect
from login.models import User, Student
from .models import Reading
from django.contrib import messages

def index(request):
    context = {
        "user": User.objects.get(id = request.session['user_id'])
    }
    return render(request, "parent_home.html", context)

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
    print(request.POST['question1'])
    print(request.POST['question2'])
    print(request.POST['question3'])
    print(request.POST['St. Patrick'])

    errors = Reading.objects.st_patty(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect back to short1.html
        return redirect('/platform/reading')
        # redirect to Good job page.
    return redirect('/platform/reading')

def st_patty_page(request):
    return render(request, 'short1.html')
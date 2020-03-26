from django.shortcuts import render, redirect
from login.models import User, Student, Reading
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
    errors = Reading.objects.st_patty(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect back to short1.html
        return redirect('/')
        # redirect to Good job page.
    return redirect('/')





def history(request):
    return render(request, 'history.html')

def gov_quiz(request):
    if request.method == 'POST':
        errors = Gov_Quiz.objects.gov_quiz_validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/gov_quiz')

    return render(request,'gov_quiz.html')

def white_house(request):
    if request.method == 'POST':
        errors = White_House_Quiz.objects.white_house_quiz_validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/white_house')

    return render(request, 'white_house_quiz.html')

def declaration(request):
    if request.method == 'POST':
        errors = Declaration_Quiz.objects.declaration_quiz_validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/declaration')

    return render(request, 'declaration.html')
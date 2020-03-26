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

<<<<<<< HEAD
def st_patty(request):
    print(request.POST['question1'])
    print(request.POST['question2'])
    print(request.POST['question3'])
    print(request.POST['St. Patrick'])

    errors = Reading.objects.st_patty(request.POST)
=======
def st_patty_page(request):
    return render(request, "short1.html")

def history(request):
    return render(request, 'history.html')

def gov_quiz(request):
    return render(request,'gov_quiz.html')

def white_house(request):
    return render(request, 'white_house_quiz.html')

def declaration(request):
    return render(request, 'declaration.html')

def generic_validator(request):
    print("   ")
    print("   ")
    print("VALIDATING")
    print("   ")
    print("   ")
    reading = Reading.objects
    errors = getattr(reading, request.POST['validator'])(request.POST)

>>>>>>> 87bec6f33932028cf6bd289495183b326c190e45
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        # redirect back to short1.html
<<<<<<< HEAD
        return redirect('/platform/reading')
        # redirect to Good job page.
    return redirect('/platform/reading')

def st_patty_page(request):
    return render(request, 'short1.html')
=======
        return redirect(f'/platform/{request.POST["validator"]}_page')
        # redirect to Good job page.
    return redirect(f'/platform/{request.POST["validator"]}_page')
>>>>>>> 87bec6f33932028cf6bd289495183b326c190e45

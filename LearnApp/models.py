from django.db import models


class Student(models.Model):
    name = models.TextField(max_length=15)
    # user 
    # reading
    birthdate = models.DateTimeField()
    grade = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reading(models.Model):
    question1 = models.CharField(max_length=1)
    question2 = models.CharField(max_length=1)
    question3 = models.CharField(max_length=1)
    question4 = models.CharField(max_length=1)
    student = models.ManyToManyField(Student, related_name="reading")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
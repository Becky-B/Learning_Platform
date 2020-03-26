from django.db import models

class Answer_manager(models.Manager):
    def st_patty(self, postData):
        errors = {}

        if postData['question1'] != '3':
            errors['question1'] = "Question 1 is incorrect."
        if postData['question2'] != '1':
            errors['question2'] = "Question 2 is incorrect."
        if postData['question3'] != '2':
            errors['question3'] = "Question 3 is incorrect."
        if postData['question4'] != '3':
            errors['question4'] = "Question 4 is incorrect."

        return errors

    def gov_quiz(self, postData):
        errors = {}

        if postData['question1'] != '3':
            errors['question1'] = 'Question 1 is incorrect'
        if postData['question2'] != '1':
            errors['question2'] = 'Questio 2 is incorrect'
        if postData['question3'] != '3':
            errors['question3'] = 'Question 3 is incorrect'
        if postData['question4'] != '2':
            errors['question4'] = 'Question 4 is incorrect'
        if postData['question5'] != '1':
            errors['question5'] = 'Question 5 is incorrect'

        return errors

    def white_house_quiz(self, postData):
        errors = {}

        if postData['question1'] != '2':
            errors['question1'] = 'Question 1 is incorrect'
        if postData['question2'] != '1':
            errors['question2'] = 'Questio 2 is incorrect'
        if postData['question3'] != '2':
            errors['question3'] = 'Question 3 is incorrect'
        if postData['question4'] != '3':
            errors['question4'] = 'Question 4 is incorrect'
        if postData['question5'] != '1':
            errors['question5'] = 'Question 5 is incorrect'

        return errors

    def declaration_quiz(self, postData):
        errors = {}

        if postData['question1'] != '1':
            errors['question1'] = 'Question 1 is incorrect'
        if postData['question2'] != '3':
            errors['question2'] = 'Questio 2 is incorrect'
        if postData['question3'] != '1':
            errors['question3'] = 'Question 3 is incorrect'
        if postData['question4'] != '3':
            errors['question4'] = 'Question 4 is incorrect'
        if postData['question5'] != '2':
            errors['question5'] = 'Question 5 is incorrect'
        if postData['question6'] != '1':
            errors['question6'] = 'Question 6 is incorrect'

        return errors

    def earth_quiz(self, postData):
        errors = {}
        if postData['question1'] != '2':
            errors['question1'] = 'Question 1 is incorrect'
        if postData['question2'] != '1':
            errors['question2'] = 'Questio 2 is incorrect'
        if postData['question3'] != '3':
            errors['question3'] = 'Question 3 is incorrect'
        if postData['question4'] != '2':
            errors['question4'] = 'Question 4 is incorrect'

        return errors
class Student(models.Model):
    name = models.TextField(max_length=15)
    # user
    # reading
    birthdate = models.DateTimeField()
    grade = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Answer_manager()

class Reading(models.Model):
    name = models.CharField(max_length=25)
    question1 = models.CharField(max_length=1)
    question2 = models.CharField(max_length=1)
    question3 = models.CharField(max_length=1)
    question4 = models.CharField(max_length=1)
    student = models.ManyToManyField(Student, related_name="reading")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Answer_manager()

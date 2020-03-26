from django.db import models
from datetime import datetime
import re
import bcrypt


class User_manager(models.Manager):
    def reg_validator(self, postData):
        errors = {}

        #name validation
        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least 2 characters."
        if not postData['name'].isalpha():
            errors['name'] = "Name can only contain letters"
        
        # student validation
        # if len(postData['student']) < 2:
        #     errors['student'] = "Student's name must be at least 2 characters."
        # if not postData['student'].isalpha():
        #     errors['student'] = "Student's Name can only contain letters"    
        
        # email validation
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address."

        email = User.objects.filter(email=postData['email'])

        if len(email) > 0:
            errors['email'] = "This email address is already registered."
        


        # password validation
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if postData["password"] != postData["confirm_password"]:
            errors["password"] = "Passwords do not match."  

        return errors  
    def login_validator(self, postData):
        errors = {}

        # email validation
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address."

        
        user = User.objects.filter(email=postData['email']) 
        if user:
            our_user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), our_user.password.encode()):
                errors['password'] = "Password does not match our records."
        else:
            errors['email'] = "Email does not match any of our records."
        
        return errors     




class User(models.Model):
    name = models.TextField(max_length=45)
    #student
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=65)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_manager()
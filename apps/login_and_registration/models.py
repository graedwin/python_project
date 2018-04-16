# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re 
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):
    def validate_reg(self, postData):
        print postData 
        errors = []
        first = postData['first_name']
        last = postData['last_name']
        email = postData['email']
        password = postData['password']
        c_password = postData['c_password']

        if len(first) is 0:
            errors.append('First Name is required')
        elif len(first) < 2:
            errors.append('First Name must be at least 2 characters')
        elif not first.isalpha():
            errors.append('First Name cannot contain numbers')
        if len(last) is 0:
            errors.append('last Name is required')
        elif len(last) < 2:
            errors.append('last Name must be at least 2 characters')
        elif not last.isalpha():
            errors.append('last Name cannot contain numbers')
        if len(email) is 0:
            errors.append('Email is required')
        elif not EMAIL_REGEX.match(email):
            errors.append('Email is invalid format')
        if len(password) is 0:
            errors.append('password is required')
        elif len(password) < 8:
            errors.append('password must be at least 8 characters')
        elif password != c_password:
            errors.append('passwords must match')
        
        if len(errors) > 0:
            # show errors to user
            return (False, errors)
        else:
            # first see if that email exists in users table
            result = self.filter(email=email)
            if len(result) > 0:
                # email exists
                errors.append('Email already exists')
                return (False, errors)
            else:
                # email doesn't exist and we can save
                new_user = self.create(
                    first_name = first,
                    last_name = last,
                    email = email,
                    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                )
                return (True, new_user)
    
    def validate_log(self, postData):
        errors = []
        password = postData['password']
        email = postData['email']
        if len(password) is 0:
            errors.append('password is required')
        if len(email) is 0:
            errors.append('Email is required')
        elif not EMAIL_REGEX.match(email):
            errors.append('Email is invalid format')
        if len(errors) > 0:
            # show errors to user
            return (False, errors)
        else: 
            # find user by email
            results = self.filter(email=email)
            if len(results) > 0:
                # we found a user with that email
                user = results[0]
                if bcrypt.checkpw(password.encode(), user.password.encode()):
                    # successful password
                    return (True, user)
                #password fails
                else:
                    errors.append('Invalid Email/Password Combo')
                    return (False, errors)
            else:
                errors.append('Invalid Email/Password Combo')
                return (False, errors)



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
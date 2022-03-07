from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyDB(models.Model):


    gender_choice = {
        ('Male', 'Male'),
        ('Female', 'Female'),
    }
    name = models.CharField(max_length=255)
    gender = models.CharField(choices=gender_choice, max_length=100)
    email = models.EmailField(max_length=254)
    file = models.FileField(upload_to='Documents/%y%m%d/')
    created_date = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['-created_date']



# This class required to formatting Team class
class MyDBAdmin(admin.ModelAdmin):

    list_display = ('name', 'gender', 'email', 'file', 'created_date')



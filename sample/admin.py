from django.contrib import admin
from .models import MyDB, MyDBAdmin
from django.contrib import admin



# Register your models here.
admin.site.register(MyDB, MyDBAdmin)

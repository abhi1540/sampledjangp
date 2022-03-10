from django.contrib import admin
from django.urls import path, include
from sample.views import Home, signin, signout, update, delete, getdata

urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('login', signin, name='login'),
    path('logout', signout, name='logout'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('getdata/<int:id>', getdata, name='getdata')
]

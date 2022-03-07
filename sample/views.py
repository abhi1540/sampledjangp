from django.views import View
from django.shortcuts import render, redirect
from .models import MyDB
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm



class Home(View):
    template_name = 'home1.html'

    def get(self, request, *args, **kwargs):
        data = MyDB.objects.order_by('-created_date')

        self.data = {

            'data' : data,

        }

        return render(request, self.template_name, self.data)



    def post(self, request, **kwargs):
        if request.method == 'POST':
            name = request.POST['name']
            gender = request.POST['gender']
            email = request.POST['email']
            file = request.FILES['sentfile']
            mydb = MyDB(name=name, gender=gender, email=email, file=file)
            mydb.save()
            messages.success(request, "Your Query Has Been Submitted!!!! We Will Get Back To You")
            return redirect("/home")


def signin(request):
    if request.user.is_authenticated:
        return redirect('/home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})



def signout(request):
    logout(request)
    return redirect('/home/login')


def update(request):
    return redirect('/home')


def delete(request):
    return redirect('/home')
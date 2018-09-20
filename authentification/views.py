from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.





def index(request):
    if User.is_authenticated:
        logout(request)

    if(request.method=='POST'):
        if(request.POST.get('test')=='sign_in'):

                username=request.POST.get('email')
                password=request.POST.get('password')

                user = authenticate(username=username, password=password)

                if(user):
                    login(request, user)
                    return redirect('details')
                else:
                    return render(request, 'index.html',locals())
        else:
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            password=request.POST.get('password')

            user = User()
            user.username=email
            user.email=email
            user.first_name=first_name
            user.last_name=last_name
            user.set_password(password)
            user.is_staff = True

            user.save()


    return render(request, 'index.html', locals())

def details(request):
    if request.user.is_authenticated():
        user=request.user

        if request.method=='POST':



            user.email =request.POST.get("email")
            user.username=request.POST.get("email")
            user.save()




        return render(request,'details.html',locals())
    else:
        return redirect('index')




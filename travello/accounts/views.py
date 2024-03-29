from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        #contact=request.POST['contact']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                    messages.info(request,"Email is already exist")
                    return redirect('register')
            else:
                user =  User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                user.save();
                messages.info(request,"User is created")
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
    else:
        return render(request,'register.html')


    #return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    return render(request,'profile.html')

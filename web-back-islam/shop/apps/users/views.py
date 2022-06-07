from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import Profile


def signup(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("mail")
        pass1 = request.POST.get("password")
        pass2= request.POST.get("password2")
        phone = request.POST.get("phone")

        if pass1 == pass2:
            if User.objects.filter(username = username).first():
                messages.error(request, "This username is already taken")
                return redirect('main-page')
            user = User.objects.create(
                username=username, 
                email=email)
            user.set_password(pass1)
            user.save()
            
            Profile.objects.create(user=user, phone=phone)

            user = authenticate(username=username, password=pass1)
            login(request, user)
            return redirect('main-page')
        else:
            messages.success(request, "Password are not similar")
    return render(request, "signup.html")   


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main-page')
        except:
            print("No such user")

    return render(request, 'login.html')
        

def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'user_profile.html', locals())



def user_update(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        bio = request.POST.get("bio")

        user.profile.bio = bio
        user.profile.save()
        return redirect(user.profile.get_absolute_url())
    return render(request, "user_profile.html")
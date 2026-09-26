from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def landingPage(request):
    return render(request, "landing.html")

def homePage(request):
    return render(request, "home.html")

def loginPage(request):
    # Code for login page
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect("home")
        
        print(username)
        print(password)

    return render(request, "login.html")


def registerPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password")
        password2 = request.POST.get("verifyPassword")
        phone = request.POST.get("phone")

        if (password1 != password2):
            return render(request, "signup.html", {"error": "Passwords do not match"})

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user=user)
        return redirect("home")
    
    return render(request, "signup.html")

def logoutUser(request):
    logout(request)
    return redirect("landing")

def profilePage(request):
    return render(request, "profile.html")
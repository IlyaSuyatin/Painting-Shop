from ast import IsNot
from turtle import home
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

from accounts.forms import CreateUserForm

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "accounts/log-in.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def signup_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CreateUserForm()
    ctx = {
        "form": form,
    }
    return render(request, "accounts/sign-up.html", ctx)


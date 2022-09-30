from ast import IsNot
from email import message
import http
from re import template
from sre_constants import SUCCESS
from turtle import home
from webbrowser import get
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.template import loader
from django.utils.crypto import get_random_string
from .models import Profile
from django.utils import timezone


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
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            template = loader.get_template("accounts/email.html")
            chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
            key = get_random_string(20, chars) + username
            link = f"http://127.0.0.1:8000/accounts/activate/{key}"
            ctx = {
                "username": username,
                "link": link
            }
            message_text = template.render(ctx)
            """send_mail("Welcome", "Message", from_email="ilya.suyatin@gmail.com", recipient_list=[email])"""
            message = EmailMessage("Welcome", message_text, to=[email])
            message.content_subtype = "html"
            message.send()
            data = {
                "username": username,
                "email": email,
                "password1": password1,
                "key": key,
            }
            form.save(data)
            return redirect("activation_sent")
    else:
        form = CreateUserForm()
    ctx = {
        "form": form,
    }
    return render(request, "accounts/sign-up.html", ctx)
def activate_key_sent(request):
    return render(request, "accounts/activate_key_sent.html")
def activation(request, key):
    profile = Profile.objects.get(key=key)
    if profile.user.is_active == False:
        if timezone.now() < profile.key_expires:
            profile.user.is_active = True
            profile.user.save()
            return redirect("activation_success")
        else:
            return redirect("signup")
def activation_success(request):
    return render(request, "accounts/activation_success.html")
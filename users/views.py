from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was successfully created")
            return redirect("login")

    context = {"form": form}
    return render(request, "registration/register.html", context)


def login_page(request):
    form = UserLoginForm
    context = {"form": form}
    return render(request, "registration/login.html", context)

from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return HttpResponse("Login page placeholder")

def register_view(request):
    return HttpResponse("Register page placeholder")

def profile_view(request):
    return HttpResponse("Profile page placeholder")
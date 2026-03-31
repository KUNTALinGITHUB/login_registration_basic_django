from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
import re

def login(request):
    context={}
    message=""
    checkit=""
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        checkit=request.POST.get('checkit')

        # Email pattern:
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Password pattern:
        # At least 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

        # Validation flags:
        email_valid = re.match(email_pattern, email)
        password_valid = re.match(password_pattern, password)

        if not email_valid:
            message="enter the valid email id "
        elif not password_valid:
            message = "Password must be 8+ chars with uppercase, lowercase, number & special char"
        else:
            message = "Login successful"

        if checkit:
            checkit="Done"
        else:
            checkit="Not done"
    context={
        'message': message,
        'checkit': checkit
    }
    return render(request, 'login.html', context)
from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def registerUser(request):
    return render(request, 'accounts/registerUser.html')

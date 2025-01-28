from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .monitor import run_security_checks

def index(request):
    run_security_checks()
    return HttpResponse("Security checks initiated.")

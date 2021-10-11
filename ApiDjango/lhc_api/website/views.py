# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.urls import path
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
    {"message": "example text"})

def date(request):
    a = datetime.now()
    return HttpResponse(f"requested on: {a}")


from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
import requests
import os

def button(request):
    return render(request, 'template.html')

def output(request):
    # data = helper()
    # data=requests.get("https://www.google.com/"

    data = []
    for i in range(10):
        data.append("Step #: " + str(i+1))
    # data=data.text
    return render(request, 'template.html', {'data': data})

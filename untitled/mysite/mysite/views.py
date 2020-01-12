from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
import requests


def button(request):
    return render(request, 'template.html')


def helper():
    import pandas as pd
    data = pd.read_csv("/Applications/everything/SBHacks/SB-Hacks-VI/dataframe.csv")
    df = pd.DataFrame(data)
    print (df)
    return df


def output(request):
    # data = helper()
    # data=requests.get("https://www.google.com/")
    data = "Hello world"
    # data=data.text
    return render(request, 'template.html', {'data': data})

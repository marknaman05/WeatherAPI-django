from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.

def homepage(request):
    #return HttpResponse("<h2>This is my Home Page</h2>")
    return render(request,'home/home.html')

def weather(request):
    city = request.GET.get('city')
    url = "http://api.weatherapi.com/v1/current.json?key=e2ffc2db133e482a86d163849223105&q={}&aqi=yes".format(city)
    res = requests.get(url)
    #print(res.text)
    json_data = json.loads(res.text)
    temp = json_data['current']['temp_c']
    print(temp)
    return HttpResponse("the weather in {} city is {}".format(city,temp))
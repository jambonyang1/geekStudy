from django.shortcuts import render

from django.http import JsonResponse
# Create your views here.


def index(request,name,age):
    output = {}
    output["name"]=name
    output["age"]=age
    output["message"] = f"hello, {age} years old {name}!"
    return JsonResponse(output)

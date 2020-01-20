from django.shortcuts import render
import requests

def home(request):
    context={}
    context['data']=json_results
    return render(request,'home.html',context)
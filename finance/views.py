from django.shortcuts import render
import json
from django.http import HttpResponse

def index(request):
    data = {'some': 'information'}
    res = json.dumps(data)
    response = HttpResponse(res)
    return response

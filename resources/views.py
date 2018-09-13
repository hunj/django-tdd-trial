from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<html><head><title>Resources</title></head><body></body></html>')
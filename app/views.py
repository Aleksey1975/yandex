from django.http import HttpResponse
from django.shortcuts import render

def index(r):
    return HttpResponse('INDEX')

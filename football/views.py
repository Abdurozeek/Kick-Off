from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Welcome to Home page<h1>")

def pageNotFound404(request, exception):
    return HttpResponseNotFound('<h1>ERROR 404</h1><h2>Page Not Found</h2>')

def serverError500(request):
    return HttpResponseNotFound('<h1>ERROR 500</h1><h2>Server Fail</h2>')

def authFail403(request, exception):
    return HttpResponseNotFound('<h1>ERROR 403</h1><h2>Not Authorized</h2>')

def badRequest400(request, exception):
    return HttpResponseNotFound('<h1>ERROR 400</h1><h2>Bad Request</h2>')
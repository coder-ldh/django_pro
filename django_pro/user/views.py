from django.shortcuts import HttpResponse

def user(request):
    return HttpResponse("hello world!")
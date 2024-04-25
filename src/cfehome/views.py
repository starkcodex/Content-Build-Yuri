from django.http import HttpResponse



def content_home(requets):
    return HttpResponse('Welcome to Content Engine.')
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Biemvenido a mi INICIO!!')
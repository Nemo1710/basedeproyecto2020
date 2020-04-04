from django.shortcuts import render



# Create your views here.

def inicio(request):
    print('hola')

    return render(request, 'sysmet/main.html')
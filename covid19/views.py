from django.shortcuts import render

# Create your views here.
from .models import CasosPorProvincia,DatosCOVID
def index(request):

    por_provincia = CasosPorProvincia.objects.filter().order_by('-Casos_positivos')
    datos_covid = DatosCOVID.objects.latest('id')
    labe=[]
    color_borde=[]
    color=[]
    cont=255
    cont2=0
    total_positivos =0
    for i in por_provincia:
        labe.append([i.Provincia])
        total_positivos=total_positivos + i.Casos_positivos
        color_borde.append('rgba(' + str(cont) + ', 30,' + str(cont2) + ', 1)')
        color.append('rgba(' + str(cont) + ', 30, ' + str(cont2) + ', 0.3)')
        cont = cont - 10.5
        cont2 = cont2 + 10.5

    dict={
        'positivostotal':total_positivos,
        'datosprovincia':por_provincia,
        'datoscovid': datos_covid,
        'color1': color_borde,
        'color2': color
    }
    return render(request, 'index.html',dict)
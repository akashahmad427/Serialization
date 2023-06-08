from django.shortcuts import render
from .models import Data
from .serializar import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

# all data in model object
def modelobject(request):
    fm = Data.objects.get(pk=1)
    #print('first data of fm = ',fm)
    serializer = StudentSerializers(fm)
    #print('this is second step data of serializer = ',serializer)
    #json_data = JSONRenderer().render(serializer.data)
    #print('this is third step of json data = ',json_data)
    #return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serializer.data)

#all data in query set.
def queryset(request):
    fm = Data.objects.all()
    #print('first data of fm = ',fm)
    serializer = StudentSerializers(fm,many = True)
    #print('this is second step data of serializer = ',serializer)
    #json_data = JSONRenderer().render(serializer.data)
    #print('this is third step of json data = ',json_data)
    #return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serializer.data,safe=False)
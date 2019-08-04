#DJANGO
from django.http import HttpResponse
import math
import json



#UTILITIES
from datetime import datetime


#Esto es una vista, a las funciones que respondes a una http
def hello_world(request):
    hora_now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current server time is {hora_now}'.format(hora_now=str(hora_now)))


def sort_integers(request):
    """ Return JSON response with sorted integers"""
    numbers = [int(i) for i in (request.GET['numbers']).split(',')]
    ordenado = sorted(numbers)
    data={
        'status':'ok',
        'numbers':ordenado,
        'message':'Integers sorted successfully.'
    }
    #import pdb; pdb.set_trace()
    return HttpResponse(
        json.dumps(data, indent=4),content_type="aplication/json")


def say_hi(request,name,age):
    """ RETURN A GETTING"""
    if (age<18): 
        message = 'Sorry {}!, you are not allowed here'.format(name)
    else:
        message = 'Hello {}!, welcome to MacbookPro'.format(name)
    return HttpResponse(message)
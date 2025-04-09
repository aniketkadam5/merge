from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Item
from django.http import HttpResponse
from django.shortcuts import render
def calculate(request):
    c=''
    try:
        if request.method=="POST":
            n1=float(request.POST.get('number1'))
            n2=float(request.POST.get('number2'))
            opr=request.POST.get('opr')
            if opr=='Addition':
                c=n1+n2
            elif opr=='Subtraction':
                 c=n1-n2
            elif opr=='Multiplication':
                 c=n1*n2
            elif opr=='Division':
                 c=n1/n2
            elif opr=='Remainder':
                 c=n1%n2
            data=Item( number1 = n1, number2=n2, operator = opr,  output= c)   
            data.save()  
    except:
        c="invalid operation..!"
        
    return render(request,'calculator.html',{'c':c})
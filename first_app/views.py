from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
def about(request):
    dict={'Name':'Noyon','Ages':22 ,'lst':['python','django','framework'],'birthday':datetime.datetime.now(),'value':'python is best'}
    return render(request,'first_app/about.html',dict)

def contact(request):
    lt={'list':[{'name':'Noyon','ages':25},{'name':'hasan','ages':21},{'name':'Mahedi','ages':20}]}
    return render(request,'first_app/contact.html',lt)

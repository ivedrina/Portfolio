from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View

def zbroj(Field1,Field2) :
    Field3=str(Field1).upper()+' '+ str(Field2).upper()
        
    return Field3


class Userview(View) :
    def get(self, request):

        Field3= request.session.get('Field3')
        if (  Field3) : del(request.session['Field3'])
        return render(request, "homework/homework_name.html", {'Field3' : Field3 })

    def post(self, request):
        Field1 = request.POST.get('Field1')
        Field2 = request.POST.get('Field2')
        Field3 = zbroj(Field1,Field2)
        request.session['Field3'] = Field3
        return redirect(request.path)

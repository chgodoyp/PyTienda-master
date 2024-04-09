from django.shortcuts import render,redirect 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import  FormularioRegistro
from django.contrib.auth.models import Group
from .forms import *
from django.contrib.auth.decorators import login_required


from .models import Direccion

from django.contrib import messages

def registro(request):
    if request.method == 'GET': 
        contexto = {
            'formulario': FormularioRegistro()
        }  
        return render(request, "registro.html", contexto)

    if request.method == 'POST': 
        datos_formulario = FormularioRegistro(data=request.POST)
        if datos_formulario.is_valid():
            datos_formulario.save()  
            user = datos_formulario.instance  
            my_group = Group.objects.get(name='normal')
            my_group.user_set.add(user) 
            messages.success(request, "Registrado Correctamente")
            return redirect('Home')
        else:
            contexto = {
                'formulario': datos_formulario,
                'errores': datos_formulario.errors
            }
            return render(request, 'registro.html', contexto)

    return redirect('Registro')



def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        print (request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")    
            contra=form.cleaned_data.get("password")    
            user=authenticate(username=nombre_usuario,password=contra)
            if user is not None:
                login(request,user)
                messages.add_message(request=request,level=messages.SUCCESS,message="Ingreso Correctamente")

                return redirect("Home")
            else:
                messages.add_message(request=request,level=messages.WARNING,message="Usuario no valido")
        else:
            messages.add_message(request=request,level=messages.WARNING,message="Informacion Incorrecta")
            ##messages.error(request,"Informacion incorrecta")
    else:
        form=AuthenticationForm()
        return render(request,"login.html",{"form":form})
    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

@login_required(redirect_field_name='login_required',login_url='Home')
def cerrar_sesion(request):
    logout(request)
    return redirect('Home')




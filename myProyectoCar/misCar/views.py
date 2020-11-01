from django.shortcuts import render
from .models import carw, usuario, slider, mision
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_autent
from django.contrib.auth.decorators import login_required
# Create your views here
def logout_vista(request):
    logout(request)
    return render(request,'web/index.html') 

def login(request):
    if request.POST:
        usuario =request.POST.get("txtNombreUser")
        password= request.POST.get("txtContrasenaUser")
        us = authenticate(request, username=usuario,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            return render(request,'web/index.html',{'user':us})
        else:
            return render(request,'web/login.html',{'msg':'usuario / contraseña incorrecta'})    
    return render(request,'web/login.html')

def index(request):
    sli= slider.objects.all()
    return render(request,'web/index.html',{'lista_slider':sli})

def galeria(request):
    insu = carw.objects.all()
    return render(request,'web/galeria.html',{'lista_insumos':insu})

@login_required(login_url='/login/')
def insumo(request):
    if request.POST:
        nombres = request.POST.get("txtNombre")
        valor = request.POST.get("txtvalor")
        desc = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")
        img =request.FILES.get("flImagen")
        ins = carw(
            nombre=nombres,
            precio=valor,
            descripcion=desc,
            stock=stock,
            imagen=img
        )
        ins.save()
        return render(request,'web/insumo.html',{'mensaje':'grabo insumo'})
    return render(request,'web/insumo.html')
@login_required(login_url='/login/')    
def registroUsuario(request):
    if request.POST:
        nombres=request.POST.get("txtNombre")
        apellidos=request.POST.get("txtApellidos")
        emails=request.POST.get("txtEmail")
        nomUser=request.POST.get("txtNombreUser")
        passw1=request.POST.get("txtPass1")
        passw2=request.POST.get("txtPass2")
        reg = usuario(
            name=nombres,
            apellido=apellidos,
            email=emails,
            user=nomUser,
            contraseña1=passw1,
            contraseña2=passw2
        )
        reg.save()
        return render(request,'web/registroUsuario.html',{'mensaje':'grabo usuario'})
    return render(request,'web/registroUsuario.html')
def vicion(request):
    mis =mision.objects.all()
    return render(request,'web/vicion.html',{'lista_mision':mis}
    )
    
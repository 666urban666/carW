from django.db import models

# Create your models here.
class usuario(models.Model):
    name= models.CharField(max_length=80 )
    apellido= models.CharField(max_length=80)
    email= models.EmailField()
    user=models.CharField(max_length=80,primary_key=True)
    contraseña1=models.CharField(max_length=40)
    contraseña2=models.CharField(max_length=40)

    def __str__(self):
        return self.user
    
class insumoss(models.Model):
    nombre=models.CharField(max_length=120, primary_key=True)
    precio=models.IntegerField()
    descripcion=models.CharField(max_length=200)
    stock=models.IntegerField()

    def __str__(self):
        return self.nombre

class carw(models.Model):
    nombre=models.CharField(max_length=120, primary_key=True)
    precio=models.IntegerField()
    descripcion=models.CharField(max_length=200)
    stock=models.IntegerField()
    imagen= models.ImageField(upload_to='imgInsumosCar',null=True)
    def __str__(self):
        return self.nombre

class slider(models.Model):
    subtitulos= models.CharField(max_length=20)
    titulo= models.CharField(max_length=20, primary_key=True)
    imagen= models.ImageField()

class vicion(models.Model):
    nombre= models.CharField(max_length=20,primary_key=True)
    descripcion= models.CharField(max_length=400)    

class mision(models.Model):
    nombre= models.CharField(max_length=20,primary_key=True)
    descripcion= models.CharField(max_length=400)
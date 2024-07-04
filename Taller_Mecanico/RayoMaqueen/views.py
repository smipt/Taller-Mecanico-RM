from django.shortcuts import render
from .models import Alumno,Genero
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
# Create your views here.

@login_required
def Principal(request):
    request.session["usuario"]=request.user.username
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'RayoMaqueen/Principal.html', context)

def index(request):
    RayoMaqueen= Alumno.objects.all()
    context={"RayoMaqueen":RayoMaqueen}
    return render(request, 'RayoMaqueen/index.html', context)


def Principal(request):
    context={}
    return render(request, 'RayoMaqueen/Principal.html', context)

def header(request):
    context={}
    return render(request, 'RayoMaqueen/header.html', context)

def Pintura(request):
    context={}
    return render(request , 'RayoMaqueen/Pintura.html', context)

def Frenos(request):
    context={}
    return render(request , 'RayoMaqueen/Frenos.html', context)

def Mantención(request):
    context={}
    return render(request , 'RayoMaqueen/Mantención.html', context)

def Formulario(request):
    context={}
    return render(request , 'RayoMaqueen/formulario.html', context)

def Contacto(request):
    context={}
    return render(request , 'RayoMaqueen/Contacto.html', context)

def home(request):
    context={}
    return render(request , 'RayoMaqueen/home.html', context)


def listadoSQL(request):
    RayoMaqueen=Alumno.objects.raw('SELECT * FROM RayoMaqueen_alumno')
    print(RayoMaqueen)
    context={"RayoMaqueen":RayoMaqueen}
    return render(request, 'RayoMaqueen/listadoSQL.html', context)

def alumnos_list(request):
    context={}
    return render(request , 'RayoMaqueen/alumnos_list.html', context)

def alumnos_add(request):
    context={}
    return render(request , 'RayoMaqueen/alumnos_add.html', context)

def alumnos_edit(request):
    context={}
    return render(request , 'RayoMaqueen/alumnos_edit.html', context)

#************************ CRUD ALUMNOS *******************

def crud(request):
    RayoMaqueen = Alumno.objects.all()
    context = {'RayoMaqueen': RayoMaqueen}
    return render(request, 'RayoMaqueen/alumnos_list.html', context)


def alumnosAdd(request):
    generos = Genero.objects.all()
    if request.method != 'POST':
        # No es un POST, por lo tanto se muestra el formulario para agregar.
        context = {'generos': generos}
        print("Datos no guardados")
        return render(request, 'RayoMaqueen/alumnos_add.html', context)
    else:
        # Es un POST, por lo tanto se recuperan los datos del formulario y se graban en la tabla.
        rut = request.POST.get("rut", "")
        nombre = request.POST.get("nombre", "")
        aPaterno = request.POST.get("paterno", "")
        aMaterno = request.POST.get("materno", "")
        fechaNac = request.POST.get("fechaNac", "")
        genero = request.POST.get("genero", None)
        telefono = request.POST.get("telefono", "")
        email = request.POST.get("mail", "")
        direccion = request.POST.get("direccion", "")
        activo = 1  # Se asigna directamente como entero.

        if genero is None:
            context = {'mensaje': "Error: Género no seleccionado.", 'generos': generos}
            return render(request, 'RayoMaqueen/alumnos_add.html', context)

        try:
            objGenero = Genero.objects.get(id_genero=genero)
            Alumno.objects.create(
                rut=rut,
                nombre=nombre,
                apellido_paterno=aPaterno,
                apellido_materno=aMaterno,
                fecha_nacimiento=fechaNac,
                id_genero=objGenero,
                telefono=telefono,
                email=email,
                direccion=direccion,
                activo=activo
            )
            context = {'mensaje': "OK, datos grabados...", 'generos': generos}
            print("Datos guardados")
        except Genero.DoesNotExist:
            context = {'mensaje': "Error: Género no encontrado.", 'generos': generos}
            print("Error: Género no encontrado")
        except IntegrityError:
            context = {'mensaje': "Error: El RUT ya está registrado.", 'generos': generos}
            print("Error: El RUT ya está registrado")

        # Si el guardado fue exitoso o no, se vuelve a renderizar la misma página.
        return render(request, 'RayoMaqueen/alumnos_add.html', context)

def alumnosUpdate(request, pk):
    alumno = Alumno.objects.get(pk=pk)
    generos = Genero.objects.all()
    if request.method != 'POST':
        # Mostrar el formulario con los datos del alumno
        context = {'alumno': alumno, 'generos': generos}
        return render(request, 'RayoMaqueen/alumnos_update.html', context)
    else:
        # Actualizar los datos del alumno
        alumno.rut = request.POST["rut"]
        alumno.nombre = request.POST["nombre"]
        alumno.apellido_paterno = request.POST["paterno"]
        alumno.apellido_materno = request.POST["materno"]
        alumno.fecha_nacimiento = request.POST["fechaNac"]
        alumno.telefono = request.POST["telefono"]
        alumno.email = request.POST["email"]
        alumno.direccion = request.POST["direccion"]
        genero = request.POST["genero"]
        
        try:
            alumno.id_genero = Genero.objects.get(id_genero=genero)
            alumno.save()
            context = {'mensaje': "OK, datos actualizados...", 'alumno': alumno, 'generos': generos}
        except Genero.DoesNotExist:
            context = {'mensaje': "Error: Género no encontrado.", 'alumno': alumno, 'generos': generos}
        
        return render(request, 'RayoMaqueen/alumnos_update.html', context)
    
    
def alumnos_del(request,pk):
    context={}
    try:
        alumno=Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje="Bien, datos eliminados..."
        RayoMaqueen = Alumno.objects.all()
        context = {'RayoMaqueen': RayoMaqueen, 'mensaje': mensaje}
        return render(request, 'RayoMaqueen/alumnos_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        RayoMaqueen = Alumno.objects.all()
        context = {'RayoMaqueen': RayoMaqueen, 'mensaje': mensaje}
        return render(request, 'RayoMaqueen/alumnos_list.html', context)

def alumnos_findEdit(request,pk):

    if pk != "":
        alumno=Alumno.objects.get(rut=pk)
        genero=Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context={'alumno':alumno,'generos':genero}
        if alumno:
            return render(request, 'RayoMaqueen/alumnos_edit.html', context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render(request, 'RayoMaqueen/alumnos_list', context)
        
def alumnosUpdate(request):

    if request.method == "POST":
        #Es un POST, por lo tanto se recupean los datos del formulario
        #y se graban en la tabla
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)

        alumno = Alumno()
        alumno.rut=rut
        alumno.nombre=nombre
        alumno.apellido_paterno=aPaterno
        alumno.apellido_materno=aMaterno
        alumno.fecha_nacimiento=fechaNac
        alumno.id_genero=objGenero
        alumno.telefono=telefono
        alumno.email=email
        alumno.direccion=direccion
        alumno.activo=1
        alumno.save()

        generos=Genero.objects.all()
        context={'mensaje':"OK, datos actualizados...",'generos':generos,'alumno':alumno }
        return render(request, 'RayoMaqueen/alumnos_list.html', context)
    
    else: 
        #no es un POST, por lo tanto se muestra el formulario para agregar
        RayoMaqueen = Alumno.objects.all()
        context={'RayoMaqueen':RayoMaqueen}
        return render(request, 'RayoMaqueen/alumnos_list.html', context)





















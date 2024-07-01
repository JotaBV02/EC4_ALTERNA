from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def layout(request):
    estudiantes = [ 'Bravo Veintemilla, Jorge', 
                    'Peña Chirinos, Carlos Joel',
                    'Torres Guzman, Henry Fabian',
                    'Villanueva Parrera, Jose Moises']
    return render(request,'layout.html', {
        'mensaje':'Intregrantes',
        'estudiantes': estudiantes
    })

def listar_cursos(request):
    return render(request,'listar_cursos.html')
    
def crear_curso(request):
    return render(request,'crear_curso.html')

def listar_carreras(request):
    return render(request,'listar_carreras.html')

def crear_carrera(request):
    return render(request,'crear_carrera.html')
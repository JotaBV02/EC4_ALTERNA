from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Course
from miapp.forms import FormCourse
from django.contrib import messages

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
    cursos = Course.objects.all();
    return render(request,'listar_cursos.html',{
        'cursos': cursos,
        'titulo': 'Listado de Cursos'
    })
    
def crear_curso(request):
    if request.method == 'POST':
        formulario = FormCourse(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            # Hay 2 formas de recuperar la información
            #Primera
            code  = data_form.get('code')
            name  = data_form.get('name')
            #Segunda
            hour = data_form['hour']
            credits = data_form['credits']
            state = data_form['state']
            #Guardar la informacion
            curso = Course(
                code = code,
                name = name,
                hour = hour,
                credits = credits,
                state = state,
            )
            curso.save()
            
            # Crear un mensaje flash (Sesión que solo se muestra 1 vez)
            messages.success(request, f'Se agregó correctamente el Curso {curso.name}')
            
            return redirect('listar_cursos')
            #return HttpResponse(code + ' -  ' + name + ' - '+ hour + ' - '+ credits + ' - ' + str(state))
    else:
        formulario = FormCourse()
        # Generamos un formulario vacío
    return render(request, 'crear_curso.html',{
        'form': formulario,
        'titulo': 'Agregar Curso'
    })
    
def eliminar_curso(request, idcourse):
    curso = Course.objects.get(pk=idcourse)
    curso.delete()
    return redirect('listar_cursos')

        
def listar_carreras(request):
    return render(request,'listar_carreras.html')

def crear_carrera(request):
    return render(request,'crear_carrera.html')
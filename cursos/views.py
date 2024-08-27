from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from django.contrib import messages
from .forms import CursoForm

# Create your views here.
def home(request):
    cursos = Curso.objects.all()
    messages.success(request, '¡Cursos listados!')    
    
    return render(request, "cursos/index.html", { "cursos" : cursos } )


def crearCurso(request):

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():   
            print("guardado...")         
            form.save()            
            messages.success(request, 'Curso creado correctamente!')
            return redirect('/')  
    else:
        form = CursoForm()        
      
    cursos = Curso.objects.all()     
    messages.warning(request, 'Codigo de curso ya existe!')  
    return render(request, 'cursos/index.html', { 'form': form, "cursos": cursos } )

    
   


# def edicionCurso(request, codigo):
#     curso = Curso.objects.get(codigo=codigo)
#     return render(request, "cursos/editarCurso.html", {"curso": curso})


def editarCurso(request, codigo):

    curso = get_object_or_404(Curso, codigo=codigo)
    print(curso)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            
            form.save()            
            messages.warning(request, f'¡Curso { curso.nombre } actualizado!')
            return redirect('/')  
    else:
        form = CursoForm(instance=curso)        
    
    return render(request, 'cursos/editarCurso.html', { 'form': form } )
    
   

def eliminarCurso(request, codigo):

    curso = Curso.objects.get(codigo=codigo)

    if request.method == "POST":        
        curso.delete()
        messages.warning(request, f'¡Curso { curso.nombre } eliminado!')        
               
        return redirect('/')  
    
    return render(request, 'cursos/eliminarCurso.html', { "curso" : curso } )

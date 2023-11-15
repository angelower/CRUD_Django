from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Patient
from .forms import PatientForm
# Create your views here.

def inicio(request):
    return render(request , 'paginas/index.html')

def about(request):
    return render(request , 'paginas/about.html')

def pacientes(request):
    pacientes = Patient.objects.all() # READ DENTRO DE UN CRUD
    return render(request , 'pacientes/index.html' , {'pacientes':pacientes})

def crear(request):
    infoPatient = PatientForm(request.POST or None)
    if infoPatient.is_valid():
        infoPatient.save()
        return redirect('pacientes')
    return render(request , 'pacientes/crear.html')

def editar(request , id):
    paciente = Patient.objects.get(id=id)
    formPatient = PatientForm(request.POST or None , instance=paciente)
    if formPatient.is_valid() and request.method == 'POST':
        formPatient.save()
        return redirect('pacientes')
    return render(request , 'pacientes/editar.html' , {'formPatient':formPatient})

def borrar(request , id):
    paciente = Patient.objects.get(id=id)
    paciente.delete()
    return redirect('pacientes')
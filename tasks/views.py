from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm, UserRegistration, UserSignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def LoginForm(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("datatodo")
        else:
            form.add_error(None, "Error de credenciales")
    else:
        form = UserRegistration()

    context = {"form": form}

    return render(request, "tasks/login.html", context)


@login_required
def modelando(request):
    datosbd = Tarea.objects.filter(usuario_tarea=request.user)
    ## Dado que se agrego un fk que asocia cada usuario con tareas se necesita hacer de esta manera
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea_incompleta = form.save(commit=False)
            tarea_incompleta.usuario_tarea = request.user
            tarea_incompleta.save()

    else:
        form = TareaForm()

    context = {"tareas": datosbd, "form": form}
    return render(request, "tasks/tareas.html", context)


@login_required
def modificando(request, pk):
    datosdb = Tarea.objects.get(pk=pk)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=datosdb)
        if form.is_valid():
            form.save()
            return redirect("datatodo")
    else:
        form = TareaForm(instance=datosdb)

    context = {"form": form}

    return render(request, 'tasks/modificar_tarea.html', context)


@login_required
def eliminar_tarea(request, pk):
    tarea_a_eliminar = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        nombre_tarea_eliminada = tarea_a_eliminar.nombre
        tarea_a_eliminar.delete()
        messages.success(
            request, f"Tarea '{nombre_tarea_eliminada}' eliminada exitosamente.")
        return redirect('datatodo')
    else:
        context = {
            'tarea': tarea_a_eliminar
        }
        return render(request, 'tasks/eliminar_tarea.html', context)


def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Cuenta creada exitosamente! Por favor, inicia sesión.")
            return redirect("login")
    else:
        form = UserSignUpForm()
    return render(request, "tasks/register.html", {"form": form})

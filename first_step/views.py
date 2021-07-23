from django.shortcuts import render, HttpResponse,redirect
from django.http.response import JsonResponse

# Redirige a la ruta "/blogs"
def root(request):
    return redirect("/blogs")

# Muestra el string "placeholder para luego mostrar una lista de todos los blogs"
def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

# Muestra el string "placeholder para mostrar un nuevo formulario para crear un nuevo blog"
def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

#redirige a la ruta "/" 
def create(request):
    return redirect("/")

# Muestra el string "placeholder para mostrar el blog numero: {number}"
def show(request,number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")

# muestra el string "placeholder para editar el blog {number}"
def edit(request,number):
    return HttpResponse(f"placeholder para editar el blog numero: {number}")

#redirige a la ruta "/" 
def destroy(request,number):
    return redirect("/blogs")

def json(request):
    return JsonResponse({'title': 'First Page Json'})

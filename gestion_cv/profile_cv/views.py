from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django import forms

#* |--------------------------------------------------------------------------
#* | Class User
#* |--------------------------------------------------------------------------

#? Clase user form
class UserForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['username', 'password', 'nombre']

#? Función para crear un usuario
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

#? Función para listar los usuarios
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

#? Función para actualizar un usuario
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

#? Función para eliminar un usuario
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})

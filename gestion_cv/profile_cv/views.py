from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django import forms

#* |-------------------------------------------------------------------------- 
#* | User Name 
#* |-------------------------------------------------------------------------- 

#? Clase user form 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'nombre']

#? Función para crear un usuario 
def user_create(request):
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
def user_update(request, user_id):
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
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})

#* |-------------------------------------------------------------------------- 
#* | Class Profile 
#* |-------------------------------------------------------------------------- 

#? Clase profile form 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'direccion', 'telefono', 'correo_electronico_1', 'correo_electronico_2', 'dni', 'url', 'biografia', 'open_to_work', 'vehicle', 'disability', 'disability_percentage', 'incorporation', 'sector', 'experiencias_laborales', 'hard_skills', 'soft_skills', 'idiomas', 'formaciones_academicas', 'voluntariados', 'proyectos', 'publicaciones', 'reconocimientos_premios', 'certificaciones_cursos']

#? Función para crear un perfil 
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {'form': form})

#? Función para listar los perfiles 
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

#? Función para actualizar un perfil 
def profile_update(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_form.html', {'form': form})

#? Función para eliminar un perfil 
def profile_delete(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'profile_confirm_delete.html', {'profile': profile})

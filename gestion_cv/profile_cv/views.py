from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django import forms
from .forms import *

# * |--------------------------------------------------------------------------
# * | User Name
# * |--------------------------------------------------------------------------


# ? Función para crear un usuario
def user_create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_list")
    else:
        form = UserForm()
    return render(request, "user_form.html", {"form": form})

# ? Función para listar los usuarios
def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})

# ? Función para actualizar un usuario
def user_update(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_list")
    else:
        form = UserForm(instance=user)
    return render(request, "user_form.html", {"form": form})

# ? Función para eliminar un usuario
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("user_list")
    return render(request, "user_confirm_delete.html", {"user": user})

# * |--------------------------------------------------------------------------
# * | Class Profile
# * |--------------------------------------------------------------------------


# ? Función para crear un perfil
def profile_create(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile_list")
    else:
        form = ProfileForm()
    return render(request, "profile_form.html", {"form": form})

# ? Función para listar los perfiles
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "profile_list.html", {"profiles": profiles})

# ? Función para actualizar un perfil
def profile_update(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile_list")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "profile_form.html", {"form": form})

# ? Función para eliminar un perfil
def profile_delete(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == "POST":
        profile.delete()
        return redirect("profile_list")
    return render(request, "profile_confirm_delete.html", {"profile": profile})

# Función para listar las HardSkills
def hardskill_list(request):
    hardskills = HardSkill.objects.all()
    return render(request, "hardskill_list.html", {"hardskills": hardskills})

# Función para crear una HardSkill
def hardskill_create(request):
    if request.method == "POST":
        form = HardSkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hardskill_list")
    else:
        form = HardSkillForm()
    return render(request, "hardskill_form.html", {"form": form})


# Función para actualizar una HardSkill
def hardskill_update(request, hardskill_id):
    hardskill = get_object_or_404(HardSkill, id=hardskill_id)
    if request.method == "POST":
        form = HardSkillForm(request.POST, instance=hardskill)
        if form.is_valid():
            form.save()
            return redirect("hardskill_list")
    else:
        form = HardSkillForm(instance=hardskill)
    return render(request, "hardskill_form.html", {"form": form})

# Función para eliminar una HardSkill
def hardskill_delete(request, hardskill_id):
    hardskill = get_object_or_404(HardSkill, id=hardskill_id)
    if request.method == "POST":
        hardskill.delete()
        return redirect("hardskill_list")
    return render(request, "hardskill_confirm_delete.html", {"hardskill": hardskill})
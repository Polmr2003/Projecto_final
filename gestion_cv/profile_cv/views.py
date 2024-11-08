from django.shortcuts import render, get_object_or_404, redirect
from .models import *
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

# * |--------------------------------------------------------------------------
# * | Class WorkExperience
# * |--------------------------------------------------------------------------

# ? Función para crear una experiencia laboral
def work_experience_create(request):
    if request.method == "POST":
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work_experience_list")
    else:
        form = WorkExperienceForm()
    return render(request, "work_experience_form.html", {"form": form})

# ? Función para listar las experiencias laborales
def work_experience_list(request):
    work_experiences = WorkExperience.objects.all()
    return render(request, "work_experience_list.html", {"work_experiences": work_experiences})

# ? Función para actualizar una experiencia laboral
def work_experience_update(request, work_experience_id):
    work_experience = get_object_or_404(WorkExperience, id=work_experience_id)
    if request.method == "POST":
        form = WorkExperienceForm(request.POST, instance=work_experience)
        if form.is_valid():
            form.save()
            return redirect("work_experience_list")
    else:
        form = WorkExperienceForm(instance=work_experience)
    return render(request, "work_experience_form.html", {"form": form})

# ? Función para eliminar una experiencia laboral
def work_experience_delete(request, work_experience_id):
    work_experience = get_object_or_404(WorkExperience, id=work_experience_id)
    if request.method == "POST":
        work_experience.delete()
        return redirect("work_experience_list")
    return render(request, "work_experience_confirm_delete.html", {"work_experience": work_experience})

# * |--------------------------------------------------------------------------
# * | Class AcademicEducation
# * |--------------------------------------------------------------------------

# ? Función para crear una educación académica
def academic_education_create(request):
    if request.method == "POST":
        form = AcademicEducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("academic_education_list")
    else:
        form = AcademicEducationForm()
    return render(request, "academic_education_form.html", {"form": form})

# ? Función para listar las educaciones académicas
def academic_education_list(request):
    academic_educations = AcademicEducation.objects.all()
    return render(request, "academic_education_list.html", {"academic_educations": academic_educations})

# ? Función para actualizar una educación académica
def academic_education_update(request, academic_education_id):
    academic_education = get_object_or_404(AcademicEducation, id=academic_education_id)
    if request.method == "POST":
        form = AcademicEducationForm(request.POST, instance=academic_education)
        if form.is_valid():
            form.save()
            return redirect("academic_education_list")
    else:
        form = AcademicEducationForm(instance=academic_education)
    return render(request, "academic_education_form.html", {"form": form})

# ? Función para eliminar una educación académica
def academic_education_delete(request, academic_education_id):
    academic_education = get_object_or_404(AcademicEducation, id=academic_education_id)
    if request.method == "POST":
        academic_education.delete()
        return redirect("academic_education_list")
    return render(request, "academic_education_confirm_delete.html", {"academic_education": academic_education})
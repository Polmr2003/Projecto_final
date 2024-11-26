from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# * |--------------------------------------------------------------------------
# * | Home
# * |--------------------------------------------------------------------------

#? Función para la página de inicio
def home(request):
    return render(request, "base.html")

# * |--------------------------------------------------------------------------
# * | Class Profile
# * |--------------------------------------------------------------------------

# ? Función para crear un perfil
def profile_create(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("profile_list")
    else:
        form = ProfileForm()
    return render(request, "profile/profile_form.html", {"form": form})

# ? Función para listar los perfiles
def profile_list(request):
    profiles = Profile_CV.objects.all()
    return render(request, "profile/profile_list.html", {"profiles": profiles})

# ? Función para actualizar un perfil
def profile_update(request, profile_id):
    profile = get_object_or_404(Profile_CV, id=profile_id)
    if request.method == "POST":
        form = ProfileForm(request.POST,  request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile_list")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "profile/profile_form.html", {"form": form})

# ? Función para eliminar un perfil
def profile_delete(request, profile_id):
    profile = get_object_or_404(Profile_CV, id=profile_id)
    if request.method == "POST":
        profile.delete()
        return redirect("profile_list")
    return render(request, "profile/profile_confirm_delete.html", {"profile": profile})

def profile_view(request, profile_id):
    profile = get_object_or_404(Profile_CV, id=profile_id)
    return render(request, 'profile/profile_view_details.html', {'profile': profile})

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
    return render(request, "work_experience/work_experience_form.html", {"form": form})

# ? Función para listar las experiencias laborales
def work_experience_list(request):
    work_experiences = WorkExperience.objects.all()
    return render(request, "work_experience/work_experience_list.html", {"work_experiences": work_experiences})

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
    return render(request, "work_experience/work_experience_form.html", {"form": form})

# ? Función para eliminar una experiencia laboral
def work_experience_delete(request, work_experience_id):
    work_experience = get_object_or_404(WorkExperience, id=work_experience_id)
    if request.method == "POST":
        work_experience.delete()
        return redirect("work_experience_list")
    return render(request, "work_experience/work_experience_confirm_delete.html", {"work_experience": work_experience})

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
    return render(request, "academic_education/academic_education_form.html", {"form": form})

# ? Función para listar las educaciones académicas
def academic_education_list(request):
    academic_educations = AcademicEducation.objects.all()
    return render(request, "academic_education/academic_education_list.html", {"academic_educations": academic_educations})

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
    return render(request, "academic_education/academic_education_form.html", {"form": form})

# ? Función para eliminar una educación académica
def academic_education_delete(request, academic_education_id):
    academic_education = get_object_or_404(AcademicEducation, id=academic_education_id)
    if request.method == "POST":
        academic_education.delete()
        return redirect("academic_education_list")
    return render(request, "academic_education/academic_education_confirm_delete.html", {"academic_education": academic_education})

# * |--------------------------------------------------------------------------
# * | Class SoftSkill
# * |--------------------------------------------------------------------------

#? Función para listar las SoftSkills
def softskill_list(request):
    softskills = SoftSkillUser.objects.all()
    return render(request, "softskill/softskill_list.html", {"softskills": softskills})

#? Función para crear una SoftSkill
def softskill_create(request):
    if request.method == "POST":
        form = SoftSkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("soft_skill_list")
    else:
        form = SoftSkillForm()
    return render(request, "softskill/softskill_form.html", {"form": form})

#? Función para actualizar una SoftSkill
def softskill_update(request, soft_skill_id):
    softskill = get_object_or_404(SoftSkillUser, id=soft_skill_id)
    if request.method == "POST":
        form = SoftSkillForm(request.POST, instance=softskill)
        if form.is_valid():
            form.save()
            return redirect("soft_skill_list")
    else:
        form = SoftSkillForm(instance=softskill)
    return render(request, "softskill/softskill_form.html", {"form": form})

#? Función para eliminar una SoftSkill
def softskill_delete(request, soft_skill_id):
    softskill = get_object_or_404(SoftSkillUser, id=soft_skill_id)
    if request.method == "POST":
        softskill.delete()
        return redirect("soft_skill_list")
    return render(request, "softskill/softskill_confirm_delete.html", {"softskill": softskill})

# * |--------------------------------------------------------------------------
# * | Class HardSkill
# * |--------------------------------------------------------------------------

#? Función para listar las HardSkills
def hardskill_list(request):
    hardskills = HardSkillUser.objects.all()
    return render(request, "hardskill/hardskill_list.html", {"hardskills": hardskills})

#? Función para crear una HardSkill
def hardskill_create(request):
    if request.method == "POST":
        form = HardSkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hard_skill_list")
    else:
        form = HardSkillForm()
    return render(request, "hardskill/hardskill_form.html", {"form": form})

#? Función para actualizar una HardSkill
def hardskill_update(request, hard_skill_id):
    hardskill = get_object_or_404(HardSkillUser, id=hard_skill_id)
    if request.method == "POST":
        form = HardSkillForm(request.POST, instance=hardskill)
        if form.is_valid():
            form.save()
            return redirect("hard_skill_list")
    else:
        form = HardSkillForm(instance=hardskill)
    return render(request, "hardskill/hardskill_form.html", {"form": form})

#? Función para eliminar una HardSkill
def hardskill_delete(request, hard_skill_id):
    hardskill = get_object_or_404(HardSkillUser, id=hard_skill_id)
    if request.method == "POST":
        hardskill.delete()
        return redirect("hard_skill_list")
    return render(request, "hardskill/hardskill_confirm_delete.html", {"hardskill": hardskill})

# * |--------------------------------------------------------------------------
# * | language
# * |--------------------------------------------------------------------------

#? Función para listar los idiomas
def language_list(request):
    languages = LanguageUser.objects.all()
    return render(request, "language/language_list.html", {"languages": languages})

#? Función para crear un idioma
def language_create(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("language_list")
    else:
        form = LanguageForm()
    return render(request, "language/language_form.html", {"form": form})

#? Función para actualizar un idioma
def language_update(request, language_id):
    language = get_object_or_404(LanguageUser, id=language_id)
    if request.method == "POST":
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect("language_list")
    else:
        form = LanguageForm(instance=language)
    return render(request, "language/language_form.html", {"form": form})

#? Función para eliminar un idioma
def language_delete(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    if request.method == "POST":
        language.delete()
        return redirect("language_list")
    return render(request, "language/language_confirm_delete.html", {"language": language})

# * |--------------------------------------------------------------------------
# * | Class Volunteering
# * |--------------------------------------------------------------------------

#? Función para listar los voluntariados
def volunteering_list(request):
    volunteerings = Volunteering.objects.all()
    return render(request, "volunteering/volunteering_list.html", {"volunteerings": volunteerings})

#? Función para crear un voluntariado
def volunteering_create(request):
    if request.method == "POST":
        form = VolunteeringForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("volunteering_list")
    else:
        form = VolunteeringForm()
    return render(request, "volunteering/volunteering_form.html", {"form": form})

#? Función para actualizar un voluntariado
def volunteering_update(request, volunteering_id):
    volunteering = get_object_or_404(Volunteering, id=volunteering_id)
    if request.method == "POST":
        form = VolunteeringForm(request.POST, instance=volunteering)
        if form.is_valid():
            form.save()
            return redirect("volunteering_list")
    else:
        form = VolunteeringForm(instance=volunteering)
    return render(request, "volunteering/volunteering_form.html", {"form": form})

#? Función para eliminar un voluntariado
def volunteering_delete(request, volunteering_id):
    volunteering = get_object_or_404(Volunteering, id=volunteering_id)
    if request.method == "POST":
        volunteering.delete()
        return redirect("volunteering_list")
    return render(request, "volunteering/volunteering_confirm_delete.html", {"volunteering": volunteering})

# * |--------------------------------------------------------------------------
# * | Class Project
# * |--------------------------------------------------------------------------

#? Función para listar los proyectos
def project_list(request):
    projects = Project.objects.all()
    return render(request, "project/project_list.html", {"projects": projects})

#? Función para crear un proyecto
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "project/project_form.html", {"form": form})

#? Función para actualizar un proyecto
def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm(instance=project)
    return render(request, "project/project_form.html", {"form": form})

#? Función para eliminar un proyecto
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        project.delete()
        return redirect("project_list")
    return render(request, "project/project_confirm_delete.html", {"project": project})

# * |--------------------------------------------------------------------------
# * | Class RecognitionAward
# * |--------------------------------------------------------------------------

#? Función para listar los reconocimientos y premios
def recognition_award_list(request):
    recognitions_awards = RecognitionAward.objects.all()
    return render(request, "recognitionaward/recognitionaward_list.html", {"recognitions_awards": recognitions_awards})

#? Función para crear un reconocimiento o premio
def recognition_award_create(request):
    if request.method == "POST":
        form = RecognitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recognition_award_list")
    else:
        form = RecognitionForm()
    return render(request, "recognitionaward/recognitionaward_form.html", {"form": form})

#? Función para actualizar un reconocimiento o premio
def recognition_award_update(request, recognition_award_id):
    recognitionaward = get_object_or_404(RecognitionAward, id=recognition_award_id)
    if request.method == "POST":
        form = RecognitionForm(request.POST, instance=recognitionaward)
        if form.is_valid():
            form.save()
            return redirect("recognition_award_list")
    else:
        form = RecognitionForm(instance=recognitionaward)
    return render(request, "recognitionaward/recognitionaward_form.html", {"form": form})

#? Función para eliminar un reconocimiento o premio
def recognition_award_delete(request, recognition_award_id):
    recognitionaward = get_object_or_404(RecognitionAward, id=recognition_award_id)
    if request.method == "POST":
        recognitionaward.delete()
        return redirect("recognition_award_list")
    return render(request, "recognitionaward/recognitionaward_confirm_delete.html", {"recognitions_awards": recognitionaward})

# * |--------------------------------------------------------------------------
# * | Class CertificationCourse
# * |--------------------------------------------------------------------------

#? Función para listar las certificaciones y cursos
def certification_course_list(request):
    certifications_courses = CertificationCourse.objects.all()
    return render(request, "certificationcourse/certificationcourse_list.html", {"certifications_courses": certifications_courses})

#? Función para crear una certificación o curso
def certification_course_create(request):
    if request.method == "POST":
        form = CertificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("certification_course_list")
    else:
        form = CertificationForm()
    return render(request, "certificationcourse/certificationcourse_form.html", {"form": form})

# Función para actualizar una certificación o curso
def certification_course_update(request, certification_course_id):
    certificationcourse = get_object_or_404(CertificationCourse, id=certification_course_id)
    if request.method == "POST":
        form = CertificationForm(request.POST, instance=certificationcourse)
        if form.is_valid():
            form.save()
            return redirect("certification_course_list")
    else:
        form = CertificationForm(instance=certificationcourse)
    return render(request, "certificationcourse/certificationcourse_form.html", {"form": form})

# Función para eliminar una certificación o curso
def certification_course_delete(request, certification_course_id):
    certificationcourse = get_object_or_404(CertificationCourse, id=certification_course_id)
    if request.method == "POST":
        certificationcourse.delete()
        return redirect("certification_course_list")
    return render(request, "certificationcourse/certificationcourse_confirm_delete.html", {"certificationcourse": certificationcourse})

# * |--------------------------------------------------------------------------
# * | Class Publication
# * |--------------------------------------------------------------------------

#? Función para listar las publicaciones
def publication_list(request):
    publications = Publication.objects.all()
    return render(request, "publication/publication_list.html", {"publications": publications})

#? Función para crear una publicación
def publication_create(request):
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("publication_list")
    else:
        form = PublicationForm()
    return render(request, "publication/publication_form.html", {"form": form})

#? Función para actualizar una publicación
def publication_update(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    if request.method == "POST":
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect("publication_list")
    else:
        form = PublicationForm(instance=publication)
    return render(request, "publication/publication_form.html", {"form": form})

#? Función para eliminar una publicación
def publication_delete(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    if request.method == "POST":
        publication.delete()
        return redirect("publication_list")
    return render(request, "publication/publication_confirm_delete.html", {"publication": publication})

# * |-------------------------------------------------------------------------- 
# * | User_CV
# * |--------------------------------------------------------------------------

#? Función para listar los CV
def user_cv_list(request):
    user_cv = User_cv.objects.all()
    return render(request, "user_cv/user_cv_list.html", {"user_cv": user_cv})

#? Función para crear un CV
def user_cv_create(request, username):
    profile_cv = get_object_or_404(Profile_CV, user__username=username)
    if request.method == "POST":
        form = UserCvForm(request.POST)
        if form.is_valid():
            user_cv = form.save(commit=False)
            user_cv.profile_cv = profile_cv # Asigna el nombre del usuario
            user_cv.save()
            return redirect("user_cv_list")
    else:
        random_numbers = ''.join(random.choices(string.digits, k=4))
        initial_urlCV = f"https://{username}-{random_numbers}.com"
        form = UserCvForm(initial={'urlCV': initial_urlCV})
    return render(request, "user_cv/user_cv_form.html", {"form": form})

#? Función para actualizar un CV
def user_cv_update(request, user_cv_id):
    user_cv = get_object_or_404(User_cv, id=user_cv_id)
    if request.method == "POST":
        form = UserCvForm(request.POST, instance=user_cv)
        if form.is_valid():
            form.save()
            return redirect("user_cv_list")
    else:
        form = UserCvForm(instance=user_cv)
    return render(request, "user_cv/user_cv_form.html", {"form": form})

#? Función para eliminar un CV
def user_cv_delete(request, user_cv_id):
    user_cv = get_object_or_404(User_cv, id=user_cv_id)
    if request.method == "POST":
        user_cv.delete()
        return redirect("user_cv_list")
    return render(request, "user_cv/user_cv_confirm_delete.html", {"user_cv": user_cv})


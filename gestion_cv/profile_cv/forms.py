from django import forms
from .models import *

# Form to represent a profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "user",
            "address",
            "phone",
            "email_1",
            "email_2",
            "dni",
            "url",
            "biography",
            "open_to_work",
            "vehicle",
            "disability",
            "disability_percentage",
            "incorporation",
            "sector",
            "work_experiences",
            "hard_skills",
            "soft_skills",
            "languages",
            "academic_educations",
            "volunteerings",
            "projects",
            "publications",
            "recognitions_awards",
            "certifications_courses",
        ]

# Form to represent a user
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "nombre"]

# Form to represent a work experience
class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = [
            "job_title",
            "start_date",
            "end_date",
            "current_job",
            "company_name",
            "description",
            "achievements",
            "references",
        ]

# Form to represent an academic education
class AcademicEducationForm(forms.ModelForm):
    class Meta:
        model = AcademicEducation
        fields = [
            "title",
            "academy_name",
            "start_date",
            "end_date",
            "current_education",
            "references",
        ]

# Form to represent a hard skill
class HardSkillForm(forms.ModelForm):
    class Meta:
        model = HardSkill
        fields = ["name", "description"]

# Form to represent a soft skill
class SoftSkillForm(forms.ModelForm):
    class Meta:
        model = SoftSkill
        fields = ["name", "description"]

# Form to represent a language
class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ["name", "level", "certifications"]

# Form to represent a volunteering
class VolunteeringForm(forms.ModelForm):
    class Meta:
        model = Volunteering
        fields = [
            "volunteering_position",
            "start_date",
            "end_date",
            "current_volunteering",
            "entity_name",
            "description",
            "achievements",
            "references",
        ]

# Form to represent a project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "link"]

# Form to represent a publication
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ["doi", "url", "role", "name"]

# Form to represent a recognition or award
class RecognitionForm(forms.ModelForm):
    class Meta:
        model = RecognitionAward
        fields = ["name", "entity", "description"]

# Form to represent a certification or course
class CertificationForm(forms.ModelForm):
    class Meta:
        model = CertificationCourse
        fields = [
            "title",
            "academy_name",
            "start_date",
            "end_date",
            "current_course",
        ]
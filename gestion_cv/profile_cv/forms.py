from django import forms
from .models import *

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

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "nombre"]

class HardSkillForm(forms.ModelForm):
    class Meta:
        model = HardSkill
        fields = ["name", 'description']

class SoftSkillForm(forms.ModelForm):
    class Meta:
        model = SoftSkill
        fields = ["name", 'description']

class languageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ["name", 'level', 'certification']


class VolunteeringForm(forms.ModelForm):
    class Meta:
        model = Volunteering
        fields = ["name", 'organization', 'description', 'start_date', 'end_date', 'current_volunteering', 'references']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", 'description', 'start_date', 'end_date', 'current_project', 'references']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ["name", 'description', 'date', 'references']

class RecognitionAwardForm(forms.ModelForm):
    class Meta:
        model = RecognitionAward
        fields = ["name", 'description', 'date', 'references']


class CertificationCourseForm(forms.ModelForm):
    class Meta:
        model = CertificationCourse
        fields = ["name", 'description', 'date', 'references']




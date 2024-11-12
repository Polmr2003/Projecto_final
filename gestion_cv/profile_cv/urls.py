"""
URL configuration for gestion_cv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [

    # Home URL
    path('', home, name='home'),

    # User URLs
    path('users/', user_list, name='user_list'),
    path('users/create/', user_create, name='user_create'),
    path('users/update/<int:user_id>/', user_update, name='user_update'),
    path('users/delete/<int:user_id>/', user_delete, name='user_delete'),

    # Profile URLs
    path('profiles/', profile_list, name='profile_list'),
    path('profiles/create/', profile_create, name='profile_create'),
    path('profiles/update/<int:profile_id>/', profile_update, name='profile_update'),
    path('profiles/delete/<int:profile_id>/', profile_delete, name='profile_delete'),

    # Work experience URLs
    path('work_experiences/', work_experience_list, name='work_experience_list'),
    path('work_experiences/create/', work_experience_create, name='work_experience_create'),
    path('work_experiences/update/<int:work_experience_id>/', work_experience_update, name='work_experience_update'),
    path('work_experiences/delete/<int:work_experience_id>/', work_experience_delete, name='work_experience_delete'),

    # Academic education URLs
    path('academic_educations/', academic_education_list, name='academic_education_list'),
    path('academic_educations/create/', academic_education_create, name='academic_education_create'),
    path('academic_educations/update/<int:academic_education_id>/', academic_education_update, name='academic_education_update'),
    path('academic_educations/delete/<int:academic_education_id>/', academic_education_delete, name='academic_education_delete'),

    # Hard skill URLs
    path('hard_skills/', hardskill_list, name='hard_skill_list'),
    path('hard_skills/create/', hardskill_create, name='hard_skill_create'),
    path('hard_skills/update/<int:hard_skill_id>/', hardskill_update, name='hard_skill_update'),
    path('hard_skills/delete/<int:hard_skill_id>/', hardskill_delete, name='hard_skill_delete'),

    # Soft skill URLs
    path('soft_skills/', softskill_list, name='soft_skill_list'),
    path('soft_skills/create/', softskill_create, name='soft_skill_create'),
    path('soft_skills/update/<int:soft_skill_id>/', softskill_update, name='soft_skill_update'),
    path('soft_skills/delete/<int:soft_skill_id>/', softskill_delete, name='soft_skill_delete'),

    # Language URLs
    path('languages/', language_list, name='language_list'),
    path('languages/create/', language_create, name='language_create'),
    path('languages/update/<int:language_id>/', language_update, name='language_update'),
    path('languages/delete/<int:language_id>/', language_delete, name='language_delete'),

    # Volunteering URLs
    path('volunteerings/', volunteering_list, name='volunteering_list'),
    path('volunteerings/create/', volunteering_create, name='volunteering_create'),
    path('volunteerings/update/<int:volunteering_id>/', volunteering_update, name='volunteering_update'),
    path('volunteerings/delete/<int:volunteering_id>/', volunteering_delete, name='volunteering_delete'),

    # Project URLs
    path('projects/', project_list, name='project_list'),
    path('projects/create/', project_create, name='project_create'),
    path('projects/update/<int:project_id>/', project_update, name='project_update'),
    path('projects/delete/<int:project_id>/', project_delete, name='project_delete'),

    # Publication URLs
    path('publications/', publication_list, name='publication_list'),
    path('publications/create/', publication_create, name='publication_create'),
    path('publications/update/<int:publication_id>/', publication_update, name='publication_update'),
    path('publications/delete/<int:publication_id>/', publication_delete, name='publication_delete'),

    # Recognition and award URLs
    path('recognitions_awards/', recognition_award_list, name='recognition_award_list'),
    path('recognitions_awards/create/', recognition_award_create, name='recognition_award_create'),
    path('recognitions_awards/update/<int:recognition_award_id>/', recognition_award_update, name='recognition_award_update'),
    path('recognitions_awards/delete/<int:recognition_award_id>/', recognition_award_delete, name='recognition_award_delete'),

    # Certification and course URLs
    path('certifications_courses/', certification_course_list, name='certification_course_list'),
    path('certifications_courses/create/', certification_course_create, name='certification_course_create'),
    path('certifications_courses/update/<int:certification_course_id>/', certification_course_update, name='certification_course_update'),
    path('certifications_courses/delete/<int:certification_course_id>/', certification_course_delete, name='certification_course_delete'),
]
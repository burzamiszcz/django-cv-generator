from django.shortcuts import render
from django.db.models import Q
from .forms import *
from .models import *

def personal_data(request):
    instance = PersonalData.objects.get(pk=1)
    if request.method == "POST":
        form = PersonalDataForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()

    form = {'PersonalDataForm': PersonalDataForm(instance = instance)}
    return render(request, 'personal_data.html', form)

def skills(request):
    if request.method == "POST":
        choicesForSkillSelection = [(skill.skill_name, skill.skill_name) for skill in Skill.objects.all()]
        skillForm = SkillForm(request.POST)
        skillSelection = SkillSelectionForm(request.POST)
        skillSelection.fields['skills'].choices = choicesForSkillSelection          

        if skillForm.is_valid():
            skillForm.save()

        if skillSelection.is_valid():
            selected_skills = skillSelection.cleaned_data
            Skill.objects.filter(skill_name__in=selected_skills['skills']).update(status=True)
            Skill.objects.filter(~Q(skill_name__in=selected_skills['skills'])).update(status=False)

    choicesForSkillSelection = [(skill.skill_name, skill.skill_name) for skill in Skill.objects.all()]
    allSkills = Skill.objects.all()
    skillForm = SkillForm()
    educationForm = EducationForm()
    certifictionForm = CertificationForm()
    skillSelection = SkillSelectionForm(initial={'skills':[skill.skill_name for skill in Skill.objects.all() if skill.status]})
    skillSelection.fields['skills'].choices = choicesForSkillSelection          
    data = {'skillForm': skillForm,
            'educationForm': educationForm,
            'certifictionForm': certifictionForm,
            'allSkills': allSkills,
            'skillsSelection': skillSelection}

    return render(request, 'skills.html', data)

def languages(request):
    allLanguages = Language.objects.all()
    languageForm = LanguageForm()

    if request.method == "POST":
        languageForm = LanguageForm(request.POST)
        if languageForm.is_valid():
            languageForm.save()
    print(allLanguages)

    data = {'languagesForm': languageForm,
            'allLanguages': allLanguages}
    return render(request, 'languages.html', data)

def education(request):
    allEducation = Education.objects.all()
    educationFrom = EducationForm()
    
    if request.method == "POST":
        educationFrom = EducationForm(request.POST)
        if educationFrom.is_valid():
            educationFrom.save()
    print(allEducation)

    data = {'educationForm': educationFrom,
            'allEducation': allEducation}
    return render(request, 'education.html', data)
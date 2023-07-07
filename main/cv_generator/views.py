from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import *
from .models import *
from datetime import datetime, date, timedelta

def personal_data(request):
    try:
        instance = PersonalData.objects.get(pk=1)
    except PersonalData.DoesNotExist:
        instance = None
    if request.method == "POST":
        form = PersonalDataForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()

    form = {'PersonalDataForm': PersonalDataForm(instance = instance)}
    return render(request, 'personal_data.html', form)


def skills(request):
    if request.method == "POST":
        if 'skill_name' not in request.POST:
            fieldOrder = request.POST['fieldOrder'].split(';')
            activeStatus = request.POST['activeStatus'].split(';')
            for i in range(len(activeStatus)):
                skill = Skill.objects.get(skill_name=fieldOrder[i])
                skill.order = i + 1
                if activeStatus[i] == 'active':
                    skill.status = "True"
                else:
                    skill.status = "False"
                skill.save()
        
        skillForm = SkillForm(request.POST)

        if skillForm.is_valid():
            skillForm.save()


    allSkills = Skill.objects.all()
    skillForm = SkillForm()

    data = {'skillForm': skillForm,
            'allSkills': allSkills}

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


def certification(request):
    allCertification = Certification.objects.all()
    certificationForm = CertificationForm()
    
    if request.method == "POST":
        certificationForm = CertificationForm(request.POST)
        if certificationForm.is_valid():
            certificationForm.save()

    data = {'certificationForm': certificationForm,
            'allCertification': allCertification}
    return render(request, 'certification.html', data)

def experience(request):
    experienceForm = ExperienceForm()
    allExperience = Experience.objects.all()
    for object in allExperience:
        object.responsibilites = object.responsibilites.split(".")
        del object.responsibilites[-1]

    if request.method == "POST":
        experienceForm = ExperienceForm(request.POST)
        if experienceForm.is_valid():
            experienceForm.save()

    data = {'experienceForm': experienceForm,
            'allExperience': allExperience}
    return render(request, 'experience.html', data)

def experienceEdit(request, id):
    experienceId = Experience.objects.get(pk=id)
    experienceForm = ExperienceForm(instance=experienceId)
    if experienceId.end_date == 'Now':
        experienceForm.fields['now_checkbox'].initial = True

    if request.method == "POST":
        experienceForm = ExperienceForm(request.POST, instance=experienceId)
        if experienceForm.is_valid():
            experienceForm.save()
        return redirect('experience')

    data = {'experienceForm': experienceForm,
            'experienceId': experienceId}
    return render(request, 'experienceEdit.html', data)

def cv(request):
    personalData = PersonalData.objects.get(pk=1)
    skillsData = Skill.objects.filter(status="True")
    languageData = Language.objects.all()
    educationData = Education.objects.all()
    certificationData = Certification.objects.all()
    experienceData = Experience.objects.all()
    experiencePeriod = []

    for object in experienceData:
        object.responsibilites = object.responsibilites.split(".")
        del object.responsibilites[-1]
        if object.end_date == 'Now':
            delta = date.today() - object.start_date
        else:
            delta = datetime.strptime(object.end_date, "%Y-%m-%d").date() - object.start_date
        total_months = delta.days // 30
        years = total_months // 12
        months = total_months % 12 + 1
        if years > 0:
            result = f"{years} years {months} months"
        else: result = f"{months} months"
        experiencePeriod.append(result)
        d = zip(list(experienceData), experiencePeriod)

    data = {'personalData': personalData,
            'skillData': skillsData,
            'languageData': languageData,
            'educationData': educationData,
            'certificationData': certificationData,
            'experienceData': d,
            'experiencePeriod': experiencePeriod}
    return render(request, 'cv_template.html', data)

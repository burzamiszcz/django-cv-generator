from django import forms
from .models import *

class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = '__all__'

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'

class ExperienceForm(forms.ModelForm):
    now_checkbox = forms.BooleanField(required=False, label="Select if it is current job")

    class Meta:
        model = Experience
        fields = ['start_date', 'end_date', 'now_checkbox', 'company_name', 'position_name', 'responsibilites']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'responsibilites': 'Responsibilities: (delimit them by \'.\' sign)'
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        now_checkbox = self.cleaned_data.get('now_checkbox')
        
        if now_checkbox:
            instance.end_date = 'Now'
        
        if commit:
            instance.save()
        
        return instance
        
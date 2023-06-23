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

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'

class SkillSelectionForm(forms.Form):
    skills = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple
    )
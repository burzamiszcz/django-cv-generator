from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PersonalData)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Experience)
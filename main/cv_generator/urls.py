from . import views
from django.urls import path

urlpatterns = [
    path('personal_data', views.personal_data, name='personal_data'),
    path('skills', views.skills, name='skills'),
    path('languages', views.languages, name='languages'),
    path('education', views.education, name='education'),
    path('certification', views.certification, name='certification'),
    path('cv', views.cv, name='cv'),
]

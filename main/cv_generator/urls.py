from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.personal_data, name='personal_data'),
    path('personal_data', views.personal_data, name='personal_data'),
    path('skills', views.skills, name='skills'),
    path('languages', views.languages, name='languages'),
    path('education', views.education, name='education'),
    path('certification', views.certification, name='certification'),
    path('experience', views.experience, name='experience'),
    path('experience/edit/<int:id>', views.experienceEdit, name='experienceEdit'),
    path('cv', views.cv, name='cv'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

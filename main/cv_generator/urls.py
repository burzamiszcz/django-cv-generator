from . import views
from django.urls import path

urlpatterns = [
    path('', views.personal_data),
    path('skills', views.skills),
    path('languages', views.languages),
    path('education', views.education),
]

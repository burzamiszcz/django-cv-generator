from . import views
from django.urls import path

urlpatterns = [
    path('', views.personal_data),
    path('skills', views.skills),
]

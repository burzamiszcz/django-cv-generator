from django.db import models

class PersonalData(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.PhoneNumberField()
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=30)
    github = models.URLField(max_length=200)
    about_me = models.TextField()

class Skills(models.Model):
    skill_name = models.CharField(max_length=50)

class Languages(models.Model):
    language = models.CharField(max_length=50)
    level = models.CharField(max_length=3)

class Educations(models.Model):
    start_date = models.DateField()
    end_date  = models.DateField()
    LEVEL_CHOICES = (
        ('Bachelor', 'Bachelor degree'),
        ('Engineer', 'Engineer degree'),
        ('Master', 'Master degree'),
    )
    level = models.CharField(verbose_name='Poziom', max_length=10, choices=LEVEL_CHOICES)

class Certifications(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

class Experiences(models.Model):
    start_date = models.DateField()
    end_date  = models.DateField()
    company_name = models.CharField(max_length=50)
    responsibilites = models.TextField()
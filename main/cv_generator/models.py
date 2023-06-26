from django.db import models

class PersonalData(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=30)
    github = models.URLField(max_length=200)
    about_me = models.TextField()
    photo = models.ImageField()

    def __str__(self) -> str:
        return self.name + self.surname

class Skill(models.Model):
    skill_name = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=False)

class Language(models.Model):
    language = models.CharField(max_length=50)
    LEVEL_CHOICES = (
        ('Na', 'Native'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
    )
    level = models.CharField(verbose_name='Level', max_length=2, choices=LEVEL_CHOICES)

class Education(models.Model):
    name = models.CharField(max_length=50)
    university_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date  = models.DateField()
    LEVEL_CHOICES = (
        ('Bachelor', 'Bachelor degree'),
        ('Engineer', 'Engineer degree'),
        ('Master', 'Master degree'),
    )
    level = models.CharField(verbose_name='Level', max_length=10, choices=LEVEL_CHOICES)

class Certification(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

class Experience(models.Model):
    start_date = models.DateField()
    end_date  = models.DateField()
    company_name = models.CharField(max_length=50)
    responsibilites = models.TextField()
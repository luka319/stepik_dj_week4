from django.db import models
from django.db.models.fields.files import ImageFieldFile
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from stepik_work.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR
from django.contrib.auth.models import User

class Company(models.Model):
    # Создайте модель «Company – компания» с полями:
    id_str = models.CharField(max_length=10)
    name = models.CharField(max_length=130)  # Название (name)
    location = models.CharField(max_length=130)  # Город (location)
    # logo = models.URLField(default='https://place-hold.it/100x60')
    logo = models.ImageField(default="",
                             upload_to=MEDIA_COMPANY_IMAGE_DIR,
                             height_field='height_field',
                             width_field='width_field')
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)
    description = models.TextField()  # Информация о компании (description)
    employee_count = models.PositiveIntegerField()
    # Количество сотрудников (employee_count)
    # owner = models.OneToOneField(User, default=0,
    #                              on_delete=models.CASCADE,
    #                              related_name = "vacancies")

    def __str__(self):
        return f"{self.name} / {self.location}/ {self.logo}"


class Speciality(models.Model):
    # Создайте модель «Specialty – специализация» с    полями:
    code = models.CharField(max_length=30)
    # Код(code)    например, testing, gamedev
    title = models.CharField(max_length=130)  # Название(title)
    # picture = models.ImageField(default='https://place-hold.it/100x60',
    picture = models.ImageField(default="",
                             upload_to=MEDIA_SPECIALITY_IMAGE_DIR,
                             height_field='height_field',
                             width_field='width_field')
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.code} / {self.title}/ {self.picture}"


class Vacancy(models.Model):
    id_str = models.CharField(max_length=10)
    title = models.CharField(max_length=120)
    # – Название  вакансии(title)
    speciality = models.ForeignKey(Speciality,
                                   on_delete=models.CASCADE,
                                   related_name="vacancies")
    # – Специализация(specialty) – связь с Specialty,
    # укажите  related_name = "vacancies"
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name="vacancies")
    # – Компания(company) – связь с  Company,
    # укажите   related_name = "vacancies"
    skills = models.CharField(max_length=255)  # – Навыки(skills)
    text = models.TextField()  # – Текст(description)
    salary_min = models.PositiveIntegerField()  # – Зарплата  от(salary_min)
    salary_max = models.PositiveIntegerField()  # – Зарплата  до(salary_max)
    published_at = models.DateField()  # – Опубликовано(published_at)

    def __str__(self):
        return self.title

# from phonenumber_field.modelfields import PhoneNumberField
# class MyModel(models.Model):
#     name = models.CharField(max_length=255)
#     phone_number = PhoneNumberField()
#     fax_number = PhoneNumberField(blank=True)
class Application(models.Model): # отклик

     written_username = models.CharField(max_length=255)
     written_phone = PhoneNumberField(blank=True)
     written_cover_letter = models.TextField()
     vacancy = models.ForeignKey(Vacancy,
                                 on_delete=models.CASCADE,
                                 related_name="applications")
     user = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="applications")

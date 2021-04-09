from django.db import models


# Create your models here.


class Company(models.Model):
    # Создайте модель «Company – компания» с полями:
    id_str = models.CharField(max_length=10)
    name = models.CharField(max_length=130)  # Название (name)
    location = models.CharField(max_length=130)  # Город (location)
    logo = models.URLField(default='https://place-hold.it/100x60')
    #  Логотипчик (logo) (URLField(default='https://place-hold.it/100x60'))
    description = models.TextField()  # Информация о компании (description)
    employee_count = models.PositiveIntegerField()
    # Количество сотрудников (employee_count)

    def __str__(self):
        return f"{self.name} / {self.location}/ {self.logo}"


class Speciality(models.Model):
    # Создайте модель «Specialty – специализация» с    полями:
    code = models.CharField(max_length=30)
    # Код(code)    например, testing, gamedev
    title = models.CharField(max_length=130)  # Название(title)
    picture = models.URLField(
        default='https://place-hold.it/100x60')
    # Картинка(picture)(URLField(default='https://place-hold.it/100x60'))

    def __str__(self):
        return f"{self.code} / {self.title}"


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

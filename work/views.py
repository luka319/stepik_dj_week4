from django.shortcuts import render
from work.models import Company, Speciality, Vacancy
# from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http import HttpResponseForbidden, HttpResponseServerError
from .forms import MySignupView, MyLoginView

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stepik_work.settings")
django.setup()



def main_view(request):  # Главная  /
    """5.    Выведите    список    специализаций    на    главной
    странице    Получите    специализации    типа «фронтенд» или «бекенд» из
    базы, выведите    их    на    главной.    Вместо    картинок    храните
    в    базе    данных    https: // place - hold.it / 100    x60
    """
    spec = Speciality.objects.all()
    spec_dict = {}
    # spec_picture_url = {}
    for spec_ in spec:
        # spec_picture_url[spec_.picture.url] = spec_.picture.url
        # spec_dict[spec_.code] = (spec_.title, spec_picture_url)
        spec_dict[spec_.code] = (spec_.title, spec_.picture.url)

    # print(f"{spec_.picture.url=}")
    # print(f"{spec_dict=}")

    spec_count = {}
    spec_picture_url = {}
    for spec2, value_tuple in spec_dict.items():
        code = Vacancy.objects.filter(speciality__code=spec2)
        code_count = code.count()
        spec_count[spec2] = {code_count: value_tuple[1]}
    # print(f"{spec_count=}")
    # for spec_ in spec:
    #     spec_picture_url[spec_.picture.url] = spec_.picture.url
    #     spec_dict[spec_.code] = [spec_.title, spec_picture_url]

    #=======================
    company_ = Company.objects.all()
    company_id_title_dict = {}
    for spec_ in company_:
        company_id_title_dict[spec_.id_str] = spec_.name
    company_title_employee_count = {}
    for spec2 in company_:
        company_title_employee_count[spec2.name] = spec2.employee_count

    company_count = {}
    comp_id_title = company_id_title_dict
    for spec2 in comp_id_title.values():
        code = Vacancy.objects.filter(company__name=spec2)
        code_count = code.count()
        company_count[spec2] = code_count

    # picture_all = Speciality.objects.all()
    # for z in picture_all.values():
    #
    #     print(f"{z=}")
    # if z['logo']:
    #     print(f"{z['logo']=}")
    # logo2 = z['logo']
    # print(f"{logo2=}")

    return render(request, "work/index.html", context={
        'spec_count': spec_count,
        'company_count': company_count,
        # 'spec_picture_url' :spec_picture_url,
    })


def vacancies(request, ):  # Все вакансии списком   /vacancies
    vacancy_all = Vacancy.objects.all()

    return render(request, "work/vacancies.html", context={
        'vacancy_all': vacancy_all,
    })


def vacancies_category(request, category):
    # Вакансии по специализации /vacancies/cat/frontend
    vacancy_cat2 = Vacancy.objects.filter(speciality__code=category)

    spec = Speciality.objects.all()
    spec_dict = {}
    for spec_ in spec:
        spec_dict[spec_.code] = spec_.title
    category = spec_dict[category]
    return render(request, "work/vacancies.html", context={
        'vacancy_all': vacancy_cat2,
        'category': category,
    })


def companies(request, id_):  # Карточка компании  /companies/345
    company_ = Company.objects.filter(id=id_)
    company_2 = []
    for group in company_:
        name = group.name
        location = group.location


    company_code = Vacancy.objects.filter(company__id_str=id_)
    logo = Company.objects.filter(id_str=id_)
    for z in logo.values():
        if z['logo']:
            # print(f"{z['logo']=}")
            logo2=z['logo']
            print(f"{logo2=}")

        # print(f"{z=}")
    return render(request, "work/company.html", context={
        'company': company_2,
        'name': name,
        'location': location,
        'company_code': company_code,
        'picture': Speciality,
        'logo2':logo2,
        # 'picture': Speciality.picture.url,
    })


def vacancy(request, id_):  # Одна вакансия /vacancies/22
    vacancy_code = Vacancy.objects.filter(id_str=id_)

    return render(request, "work/vacancy.html", context={
        'vacancy_code': vacancy_code,
    })

def send_resume(request, vacancy_id): #  Отправка   заявки / vacancies / < vacancy_id > / send /
    return render(request, "work/send_resume.html", context={
        # 'vacancy_code': vacancy_code,
    })

def letsstart_company(request): # Моя компания (предложение создать) /mycompany/letsstart/
    return render(request, "work/letsstart_company.html", context={
        # 'vacancy_code': vacancy_code,
    })


def mycompany_create(request): # Моя компания (пустая форма) /mycompany/create/
    return render(request, "work/mycompany_create.html", context={
        # 'vacancy_code': vacancy_code,
    })


def mycompany_fill(request): # – Моя компания (заполненная форма) /mycompany/
    return render(request, "work/mycompany_fill.html", context={
        # 'vacancy_code': vacancy_code,
    })


def mycompany_vacancies(request):
    # Мои вакансии (список) /mycompany/vacancies/
    return render(request, "work/mycompany_vacancies.html", context={
        # 'vacancy_code': vacancy_code,
    })


def mycompany_vacancies_create(request):
    # – Мои вакансии (пустая форма) /mycompany/vacancies/create/
    return render(request, "work/mycompany_vacancies_create.html", context={
        # 'vacancy_code': vacancy_code,
    })


def mycompany_vacancies_vacancy_id(request):
    # – Одна моя вакансия (заполненная форма)  /mycompany/vacancies/<vacancy_id>
    return render(request, "work/mycompany_vacancies_vacancy_id.html", context={
        # 'vacancy_code': vacancy_code,
    })

# from .forms import MySignupView
def mySignup(request): # register
    signup_form = MySignupView()
    return render(request, 'signup.html', {'form': signup_form})

# def myLogin(request):
#     login_form = MyLoginView()
#     return render(request, 'accounts/login.html', {'form': login_form})


def custom_handler404(request, exception):
    return HttpResponseNotFound('<h1> Кот 404! Вот как, как Вас угораздило сюда попасть!? \
      Здесь ничего нет! Ой, это я в виноват перед Вами! Простите извините!')


def custom_handler400(request, exception):
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    return HttpResponseForbidden('Доступ запрещен!')


# def custom_handler404(request, exception):
#     return HttpResponseNotFound('Ресурс не найден!')

def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')

# stepik django 1.24.10 https://stepik.org/lesson/356368/step/10?unit=340485

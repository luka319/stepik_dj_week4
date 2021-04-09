from django.shortcuts import render
from work.models import Company, Speciality, Vacancy
# from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http import HttpResponseForbidden, HttpResponseServerError


def main_view(request):  # Главная  /
    """5.    Выведите    список    специализаций    на    главной
    странице    Получите    специализации    типа «фронтенд» или «бекенд» из
    базы, выведите    их    на    главной.    Вместо    картинок    храните
    в    базе    данных    https: // place - hold.it / 100    x60
    """
    spec = Speciality.objects.all()
    spec_dict = {}
    for spec_ in spec:
        spec_dict[spec_.code] = spec_.title

    spec_count = {}
    for spec2 in spec_dict.keys():
        code = Vacancy.objects.filter(speciality__code=spec2)
        code_count = code.count()
        spec_count[spec2] = code_count

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

    return render(request, "work/index.html", context={
        'spec_count': spec_count,
        'company_count': company_count,
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

    return render(request, "work/company.html", context={
        'company': company_2,
        'name': name,
        'location': location,
        'company_code': company_code,
    })


def vacancy(request, id_):  # Одна вакансия /vacancies/22
    vacancy_code = Vacancy.objects.filter(id_str=id_)

    return render(request, "work/vacancy.html", context={
        'vacancy_code': vacancy_code,
    })


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

"""stepik_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work.views import main_view
from work.views import vacancies  # Все вакансии списком   /vacancies
from work.views import vacancies_category
# Вакансии по специализации /vacancies/cat/frontend
from work.views import companies  # Карточка компании  /companies/345
from work.views import vacancy  # Одна вакансия /vacancies/22

from work.views import custom_handler400, custom_handler403
from work.views import custom_handler404, custom_handler500
# stepik django 1.24.10 https://stepik.org/lesson/356368/step/10?unit=340485
from django.conf import settings
from django.conf.urls.static import static


handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

from work.views import send_resume, letsstart_company
from work.views import mycompany_create,mycompany_fill
from work.views import mycompany_vacancies, mycompany_vacancies_create
from work.views import mycompany_vacancies_vacancy_id
from work import forms
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacancies/', vacancies),  # Все вакансии списком   /vacancies
    path('', main_view),  # Главная  /

    path('vacancies/cat/<str:category>/', vacancies_category),
    # Вакансии по специализации /vacancies/cat/frontend
    path('companies/<int:id_>/', companies),
    # Карточка компании  /companies/345
    path('vacancies/<int:id_>/', vacancy),  # Одна вакансия /vacancies/22

    path('vacancies/<int:vacancy_id>/send/', send_resume),
    #  Отправка   заявки / vacancies / < vacancy_id > / send /
    path('mycompany/letsstart/', letsstart_company),
    # Моя компания (предложение создать) /mycompany/letsstart/
    path('mycompany/create/', mycompany_create),
    # Моя компания (пустая форма) /mycompany/create/
    path('mycompany/', mycompany_fill),
    # – Моя компания (заполненная форма) /mycompany/
    path('mycompany/vacancies/', mycompany_vacancies),
    # Мои вакансии (список) /mycompany/vacancies/
    path('mycompany/vacancies/create/', mycompany_vacancies_create),
    # – Мои вакансии (пустая форма) /mycompany/vacancies/create/
    path('mycompany/vacancies/<int:vacancy_id>/', mycompany_vacancies_vacancy_id),
    # – Одна моя вакансия (заполненная форма)  /mycompany/vacancies/<vacancy_id>
    path('login/', forms.MyLoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', forms.MySignupView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

#========================



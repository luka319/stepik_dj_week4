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

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacancies/', vacancies),  # Все вакансии списком   /vacancies
    path('', main_view),  # Главная  /

    path('vacancies/cat/<str:category>/', vacancies_category),
    # Вакансии по специализации /vacancies/cat/frontend
    path('companies/<int:id_>/', companies),
    # Карточка компании  /companies/345
    path('vacancies/<int:id_>/', vacancy),  # Одна вакансия /vacancies/22
]

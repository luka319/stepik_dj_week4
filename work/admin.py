from django.contrib import admin
# Register your models here.
from .models import Company, Application, Vacancy, Speciality


class CompanyAdmin(admin.ModelAdmin):
    pass

class ApplicationAdmin(admin.ModelAdmin):
    pass

class VacancyAdmin(admin.ModelAdmin):
    pass

class SpecialityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Application, ApplicationAdmin)

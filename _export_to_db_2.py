from work.models import Company, Speciality, Vacancy
# сохранение данных в бд
from data import jobs, companies, specialties


for firm in companies:
    group = Company()
    group.id_str = firm["id"]
    group.name = firm["title"]
    group.location = firm["location"]
    # group.logo = firm["logo"]
    group.description = firm["description"]
    group.employee_count = int(firm["employee_count"])
    group.save()

for specia in specialties:
    spec = Speciality()
    spec.code = specia["code"]
    spec.title = specia["title"]
    # spec.picture =
    spec.save()


# for job in jobs:
for vacancy_data in jobs:
    # person = Vacancy()
    Vacancy.objects.create(
        speciality=Speciality.objects.get(code=vacancy_data['specialty']),
        company=Company.objects.get(id_str=int(vacancy_data['company'])),
        id_str=vacancy_data["id"],
        title=vacancy_data["title"],
        salary_min=int(vacancy_data["salary_from"]),
        salary_max=int(vacancy_data["salary_to"]),
        published_at=vacancy_data["posted"],
        skills=vacancy_data["skills"],
        text=vacancy_data["description"],
    )

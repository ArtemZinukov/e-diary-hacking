import random

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject, Teacher)

STUDENT_PRAISES = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!",
                   "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!",
                   "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!",
                   "Ты, как всегда, точен!", "Очень хороший ответ!", "Талантливо!",
                   "Ты сегодня прыгнул выше головы!", "Я поражен!", "Уже существенно лучше!"]


def definition_schoolkid(name):
    try:
        name_schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return name_schoolkid
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем {name_schoolkid} в БД не найден!")
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с таким именем {name_schoolkid}")


def fix_marks(schoolkid):
    name_schoolkid = definition_schoolkid(schoolkid)
    Mark.objects.filter(schoolkid=name_schoolkid, points__lte=3).update(points=5)


def remove_chastisements(schoolkid):
    name_schoolkid = definition_schoolkid(schoolkid)
    Chastisement.objects.filter(schoolkid=name_schoolkid).delete()


def get_subject(subject, schoolkid):
    try:
        subject = Subject.objects.get(title=subject, year_of_study=schoolkid.year_of_study)
        return subject
    except Subject.DoesNotExist:
        print(f"Такого предмета {subject} нет в БД")


def create_commendation(schoolkid, subject):
    name_schoolkid = definition_schoolkid(schoolkid)
    subject = get_subject(subject, name_schoolkid)
    lesson = Lesson.objects.filter(year_of_study=name_schoolkid.year_of_study, subject=subject).order_by('?').first()
    if lesson:
        Commendation.objects.filter(schoolkid=name_schoolkid, subject=subject).create(text=random.choice(STUDENT_PRAISES),
                                                                            schoolkid=name_schoolkid, subject=subject,
                                                                            teacher=lesson.teacher, created=lesson.date)

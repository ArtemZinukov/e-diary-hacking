from datacenter.models import *
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import random


def definition_name(name):
    try:
        name = Schoolkid.objects.get(full_name__contains=name)
        return name
    except ObjectDoesNotExist:
        print(f"Ученик с именем {name} в БД не найден!")
    except MultipleObjectsReturned:
        print(f"Найдено несколько учеников с таким именем {name}")


def fix_marks(schoolkid):
    name = definition_name(schoolkid)
    Mark.objects.filter(schoolkid=name, points__lte=3).update(points=5)


def remove_chastisements(schoolkid):
    name = definition_name(schoolkid)
    Chastisement.objects.filter(schoolkid=name).delete()


def choice_subject(subject, schoolkid):
    try:
        subject = Subject.objects.get(title=subject, year_of_study=schoolkid.year_of_study)
        return subject
    except ObjectDoesNotExist:
        print(f"Такого предмета {subject} нет в БД")


def create_commendation(schoolkid, subject):
    student_praises = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!",
                       "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!",
                       "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!",
                       "Ты, как всегда, точен!", "Очень хороший ответ!", "Талантливо!",
                       "Ты сегодня прыгнул выше головы!", "Я поражен!", "Уже существенно лучше!"]
    name = definition_name(schoolkid)
    subject = choice_subject(subject, name)
    lesson = Lesson.objects.filter(year_of_study=name.year_of_study, subject=subject).order_by('?').first()
    if lesson:
        Commendation.objects.filter(schoolkid=name, subject=subject).create(text=random.choice(student_praises),
                                                                            schoolkid=name, subject=subject,
                                                                            teacher=lesson.teacher, created=lesson.date)

# Данный скрипт помогает вносить изменения в школьный дневник

Данный скрипт помогает школьникам вносить корректировки в электронный дневник, такие как:
1. Изменить все плохие оценки на отличные
2. Убрать все замечания от учителей
3. Добавить похвалу по любому предмету

### Как установить

- Для установки необходимо сохранить файл scpirts.py у себя на компьютере.
- Запустить Python Shell, используя команду:
```
python manage.py shell 
```
- Далее загрузить скрипт в консоль:
```
from scripts import determine_schoolkid, fix_marks, remove_chastisements, get_subject, create_commendation
```

### Как пользоваться скриптом

Если необходимо исправить все плохие оценки, необходимо прописать команду:
```
fix_marks(name),
где name - имя ученика, писать в " " и с заглавной буквы. 
Например: fix_marks("Иванов Иван")
```

При необходимости убрать все замечания, потребуется следующая команда:
```
remove_chastisements(name),
где name - имя ученика, писать в " " и с заглавной буквы.
Например: remove_chastisements("Иванов Иван")
```
И если вы хотите написать себе похвалу от учителя, то воспользуйтесь командой:
```
create_commendation(name, subject),
где name - имя ученика, писать в "" и с заглавной буквы,
а subject - предмет, по которому хотите получить похвалу, писать в " " и с заглавной буквы.
Например: create_commendation("Иванов Иван", "Математика")
```


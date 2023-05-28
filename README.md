### Radious - небольшой агрегатор онлайн радио

Список радио взят с https://espradio.ru/stream_list/

Сервис в стадии прототипа, много функций еще не доделано.

## Запуск

Клонируем репозиторий

Создаем виртуальной окружение и активируем:

`python3.10 -m venv evnv`

`source ./env/bin/activate`

Устанавлеваем зависимости

`pip install -r requirements.txt`

Делаем миграцию БД

`python manage.py migrate`

Запускаем

`python manage.py runserver`

В репозитории добалена тестовая база

admin:admin

![Alt text](/screenshots/scr1.png?raw=true "Главная страница")
![Alt text](/screenshots/scr2.png?raw=true "Страница с конкретной станцией")
![Alt text](/screenshots/scr3.png?raw=true "Главная страница")
![Alt text](/screenshots/scr4.png?raw=true "Жанры станций")
![Alt text](/screenshots/scr5.png?raw=true "Список станций")

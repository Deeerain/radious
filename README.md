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

Делаем миграцию БД, загружаем список радиостанций и сосздаем пользователя

`python manage.py migrate`

`python manage.py fill_radio_stations`

`python manage.py createsuperuser`

Запускаем

`python manage.py runserver`

![Alt text](/screenshots/home.png?raw=true "Главная страница")
![Alt text](/screenshots/station_list.png?raw=true "Страница списка станций")
![Alt text](/screenshots/station_by_ganre.png?raw=true "Страница страниций отфильтрованных по жанру")
![Alt text](/screenshots/station_detail.png?raw=true "Страница станции")

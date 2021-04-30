# TEST

#### Версия Python == 3.9.2

#### Запуск приложения

1. Создать виртуальное окружение:
`python3.9 -m venv venv`
1. Активировать виртуальное окружение:
    * Для Windows:
    `.\venv\Scripts\sctivate`
    * Для Linux:
    `source /venv/bin/activate`
1. Установить зависимости:
`pip install -r requirements.txt`
1. Выполнить миграции:
`python manage.py migrate`
1. Запуск:
`python manage.py runserver`


#### Swagger
`localhost:8000/swagger/`
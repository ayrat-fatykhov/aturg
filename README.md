# Тестовое задание для Aturg

## Задание
Написать API для логов с аутентификацией и поиском в теле для запроса.

## Запуск проекта
- Клонировать репозиторий
- Установить зависимости (команда в терминале: poetry install)
- Активировать виртуальное окружение (poetry shell) 
- Создать файл .env, заполнить его данными из файла .env.sample
- Создать базу данных в postresql
- Создать (python manage.py makemigrations) и применить миграции (python3 manage.py migrate)
- Создать суперпользователя (python3 manage.py createsuperuser)
- Загрузить данные в базу данных (python3 manage.py loaddata db.json)
- Запустить проект "python manage.py runserver"

## Документация к API
- зарегистрировать пользователя - POST/http://localhost:8000/users/register
- получить токена - POST/http://localhost:8000/users/token/
- создать лог - POST/http://localhost:8000/logs/create
- получить список логов - GET/http://localhost:8000/logs/
- получить лог - GET/http://localhost:8000/logs/view/5
- изменить лог - PATCH/http://localhost:8000/logs/update/5
- удалить лог - DELETE/http://localhost:8000/logs/delete/5
- поиск лога - GET/http://localhost:8000/logs/search/ (отправить в теле "name" или "date"; или оба пункта сразу)

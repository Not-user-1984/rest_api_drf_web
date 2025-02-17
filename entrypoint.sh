#!/bin/sh

cd src
# Очистка базы данных
python manage.py flush --no-input
# Применение миграций
python manage.py migrate
# Генерация данных
python manage.py generate_data
# Запуск Gunicorn
gunicorn --bind 0.0.0.0:8000 config.wsgi:application

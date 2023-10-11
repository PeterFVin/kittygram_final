# Проект «taski-docker» V1.0

## О проекте

Проект Kittygram - социальная сеть для обмена фотографиями любимых питомцев

### Использованные технологии: 

 - Docker
 - Python 3.9 
 - Django==3.2.3 
 - djangorestframework==3.12.4 
 - Nginx 
 - gunicorn
 - React

### Автор проекта:

Петр Виноградов, python plus, когорта 25+

### Как запустить проект: 

- В корневой папке проекта запустить Docker Compose

sudo docker compose -f docker-compose.production.yml up -d

- Выполнить миграции

sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate

- Собрать статику бэкенда

sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic

- Скопировать статику бэкендав папку /backend_static/static/

sudo docker compose -f docker-compose.production.yml exec backend cp -r /collected_static/. /backend_static/static/

### В проекте нужен .env файл 

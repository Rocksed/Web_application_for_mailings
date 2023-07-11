# mailing_list
- **Сервис управления рассылками, администрирования и получения статистики.**

# Запуск на Windows

## **Для начала установите зависимости проекта, указанные в файле `requirements.txt`

pip install -r requirements.txt

## **Далее установите redis глобально себе на компьютер, используйте wsl, терминал Ubuntu

sudo apt-get update
sudo apt-get install redis

После установки запустите сервер Redis с помощью:

sudo service redis-server start

## Создайте файл `.env`
Введите туда свои настройки как указано в файле `.env.sample`

EMAIL_HOST_USER =
EMAIL_HOST_PASSWORD =

NAME=
USER=
PASSWORD=
BACKEND=
LOCATION=

SECRET_KEY=

## Выполните `migrate`

python manage.py migrate

# Для запуска веб сервиса для начала запустите в терминале Ubuntu redis:

redis-cli

## Затем уже в обычном терминале(Windows) запускайте сервис:

python manage.py runserver




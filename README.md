# Project Simple 3 Django REST Framework (P-S-3-DRF)

```sh
python3.8 -m venv env

source env/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

cp inventory/.env.example inventory/.env

API_KEY
python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'

SECRET_KEY
python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'

su
su postgres
psql
create database p_s_3_drf;
\q

nano inventory/.env

python manage.py migrate

python manage.py createsuperuser --email admin@example.com --username admin
python manage.py createsuperuser --email test@example.com --username test

python manage.py runserver
```
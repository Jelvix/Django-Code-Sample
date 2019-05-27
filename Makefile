# general
MANAGE=manage.py
COVERAGE=coverage
COVER=apps

DOCKER_COMPOSE=docker-compose
DOCKER_DEV_CONFIG=docker-compose.yml
CELERY_CONFIG=testcms.celery_config

pip:
	pip install --upgrade pip && pip install -r requirements.txt

python:
	python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000

celery:
	celery -A $(CELERY_CONFIG) worker -l INFO

celery_beat:
	rm -f celerybeat-schedule.db && rm -f celerybeat.pid && celery -A $(CELERY_CONFIG) beat

static:
	python3 manage.py collectstatic --noinput

flower:
	flower -A $(CELERY_CONFIG) --port=5555

docker_stop:
	$(DOCKER_COMPOSE) -f $(DOCKER_DEV_CONFIG) stop

docker_start:
	$(DOCKER_COMPOSE) -f $(DOCKER_DEV_CONFIG) up

docker_rebuild:
	$(DOCKER_COMPOSE) -f $(DOCKER_DEV_CONFIG) up --build

migrate:
	python3 manage.py migrate

install_devs:
	pip install -r requirements.txt

install_prods:
	pip install -r requirements.txt

run_server:
	python3 manage.py runserver 0.0.0.0:8000

run_gunicorn:
	inv run_it

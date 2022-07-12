PATH := $(PATH)
SHELL := /bin/bash

black:
	black --check --line-length 120 --exclude "/(\.eggs|\.git|\.hg|\.mypy _cache|\.nox|\.tox|\.venv|pgdata|_build|buck- out|build|dist|migrations|node_modules)/" ./

flake:
	flake8 -v ./

linters:
	make flake
	make black

black-format:
	black --line-length 120 --exclude "/(\.eggs|\.git|\.hg|\.mypy _cache|\.nox|\.tox|\.venv|pgdata|_build|buck- out|build|dist|migrations|node_modules)/" ./

format:
	make black-format

migrate:
	docker-compose run --rm api python manage.py migrate

fake-migrate:
	docker-compose run --rm api python manage.py migrate --fake-initial
	
migrations:
	docker-compose run --rm api python manage.py makemigrations

shell:
	docker-compose run --rm api python manage.py shell

superuser:
	docker-compose run --rm api sh -c "echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'tajne')\" | python manage.py shell" 

test:
	docker-compose run --rm -e DJANGO_SETTINGS_MODULE=settings.test api python manage.py test


DOCKER_RUN=docker compose -f local.yml

up:
	${DOCKER_RUN} up

stop:
	${DOCKER_RUN} stop

build:
	${DOCKER_RUN} build --no-cache

createuser:
	${DOCKER_RUN} exec api-menu ./src/manage.py createsuperuser

makemigrations:
	${DOCKER_RUN} exec api-menu ./src/manage.py makemigrations

migrate:
	${DOCKER_RUN} exec api-menu ./src/manage.py migrate

DOCKER_LOCAL=docker compose -f local.yml

DOCKER_PROD=docker compose -f production.yml

up:
	${DOCKER_LOCAL} up -d

up-prod:
	${DOCKER_PROD} up

stop:
	${DOCKER_LOCAL} stop

down:
	${DOCKER_LOCAL} down

down-prod:
	${DOCKER_PROD} down

build:
	${DOCKER_LOCAL} build --no-cache

build-prod:
	${DOCKER_PROD} build --no-cache

logs:
	${DOCKER_LOCAL} logs -f

logs-prod:
	${DOCKER_PROD} logs -f

attach:
	docker attach api-menu-local

createuser:
	${DOCKER_LOCAL} exec api-menu-local ./src/manage.py createsuperuser

makemigrations:
	${DOCKER_LOCAL} exec api-menu-local ./src/manage.py makemigrations

migrate:
	${DOCKER_LOCAL} exec api-menu-local ./src/manage.py migrate

rm-all:
	docker compose -f production.yml down && docker compose -f production.yml down --volumes && docker rmi -f  event-menu-nginx-menu event-menu-api-menu

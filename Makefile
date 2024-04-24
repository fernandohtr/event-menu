DOCKER_RUN=docker compose -f local.yml

up:
	${DOCKER_RUN} up -d

stop:
	${DOCKER_RUN} stop

down:
	${DOCKER_RUN} down

build:
	${DOCKER_RUN} build --no-cache

logs:
	${DOCKER_RUN} logs -f

attach:
	docker attach api-menu

createuser:
	${DOCKER_RUN} exec api-menu ./src/manage.py createsuperuser

makemigrations:
	${DOCKER_RUN} exec api-menu ./src/manage.py makemigrations

migrate:
	${DOCKER_RUN} exec api-menu ./src/manage.py migrate

DOCKER_RUN=docker compose -f local.yml

up:
	${DOCKER_RUN} up

stop:
	${DOCKER_RUN} stop

createuser:
	${DOCKER_RUN} exec api-menu ./src/manage.py createsuperuser

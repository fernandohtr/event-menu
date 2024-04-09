up:
	docker compose -f local.yml up

stop:
	docker compose -f local.yml stop

createuser:
	docker compose -f local.yml exec api-menu ./src/manage.py createsuperuser

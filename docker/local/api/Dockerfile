FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./api/requirements/local.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./docker/local/api/start.sh /start.sh
RUN sed -i ' s/\r$//g' /start.sh
RUN chmod +x /start.sh

COPY ./docker/local/api/entrypoint.sh /entrypoint.sh
RUN sed -i ' s/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE config.settings.local

ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]

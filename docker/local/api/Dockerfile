FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./api/requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./docker/local/api/start.sh /start.sh

RUN chmod +x /start.sh

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=config.settings.local

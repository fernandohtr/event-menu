FROM python:3.12-alpine AS dependencies
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./api/requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ./api/src ./src
ENTRYPOINT ["python3"]
EXPOSE 8000
CMD ["src/manage.py", "runserver", "0.0.0.0:8000"]

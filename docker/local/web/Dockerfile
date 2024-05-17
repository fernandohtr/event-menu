FROM node:20.12-alpine

WORKDIR /cache

COPY ./web/package.json ./web/package-lock.json ./

RUN npm i

COPY ./docker/local/web/start.sh /start.sh

RUN chmod +x /start.sh

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH
ENV VITE_API_URL http://localhost:8000

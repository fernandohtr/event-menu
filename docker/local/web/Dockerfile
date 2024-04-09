FROM node:20.12-alpine

WORKDIR /app

COPY ./web/package.json ./web/package-lock.json ./

RUN npm i

CMD [ "npm", "run", "dev" ]


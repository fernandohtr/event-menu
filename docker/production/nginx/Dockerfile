FROM node:20.12-alpine AS dependencies
WORKDIR /app
COPY ./web/package.json ./web/package-lock.json ./
RUN npm ci --only=production

FROM dependencies AS build
ENV VITE_API_URL http://localhost:8080
WORKDIR /app
COPY ./web/ .
RUN npm run build

FROM nginx:1.25-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

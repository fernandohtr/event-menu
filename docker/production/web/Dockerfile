FROM node:20.12-alpine AS dependencies
WORKDIR /app
COPY ./web/package.json ./web/package-lock.json ./
RUN npm ci --only=production

FROM dependencies AS build
WORKDIR /app
COPY ./web/ .
RUN npm run build

FROM dependencies AS deploy
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/package.json ./package.json
COPY --from=build /app/vite.config.ts ./vite.config.ts
RUN npm i --only=production
RUN npm i vite
EXPOSE 8080
CMD [ "npm", "run", "preview" ]

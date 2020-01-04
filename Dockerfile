# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY . .
RUN sh build.sh

# production stage
FROM nginx:alpine as production-stage
WORKDIR /app
COPY . .
COPY --from=build-stage /app/dist /app/dist
COPY nginx.conf /etc/nginx/conf.d/
RUN rm /etc/nginx/conf.d/default.conf \
    && mv /etc/nginx/conf.d/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
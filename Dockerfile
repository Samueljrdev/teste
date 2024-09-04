FROM nginx:alpine

LABEL maintainer="vitorsouza23 <vitinls387@gmail.com>"
LABEL version="1.0"

COPY . /usr/share/nginx/html/


FROM nginx:latest

RUN /etc/init.d/nginx start
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/

CMD ["nginx", "-g", "daemon off;"]

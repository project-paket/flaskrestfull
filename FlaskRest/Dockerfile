FROM python:3.6

ENV MONGO_USERNAME = "admin_name"
ENV MONGO_PASSWORD = "1234"

WORKDIR /FlaskRest

ADD . /FlaskRest

RUN pip install -r requirements.txt

CMD ["uwsgi", "--http", "0.0.0.0:80", "--wsgi-file", "views.py", \
    "--callable", "app", "--stats", "0.0.0.0:81"]
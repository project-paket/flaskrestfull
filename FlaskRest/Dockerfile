FROM python:3.6

WORKDIR /FlaskRest

COPY . /FlaskRest

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]

FROM python:3.10-alpine


WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt

RUN gunicorn config.wsgi:application --bind 0.0.0.0:8080

EXPOSE 8000

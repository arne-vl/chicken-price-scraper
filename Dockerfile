# syntax=docker/dockerfile:1

FROM python:3.10.6-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN apt-get update && apt-get -y install cron

RUN python3 manage.py crontab add

RUN service cron start

CMD ["sh", "-c", "python3 manage.py wait_for_db && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]


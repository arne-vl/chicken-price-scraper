# syntax=docker/dockerfile:1

FROM python:3.10.6-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN python3 manage.py crontab add

RUN python3 manage.py migrate

CMD ["sh", "-c", "python3 manage.py runserver 0.0.0.0:8000 && python3 manage.py"]

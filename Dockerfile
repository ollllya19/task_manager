# Dockerfile
FROM python:3.9
WORKDIR /opt/django-app
COPY . /opt/django-app/
RUN apt install -y default-libmysqlclient-dev
RUN pip install -r requirements.txt

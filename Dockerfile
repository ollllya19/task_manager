# Dockerfile
FROM python:3.11
ENV APP_PORT 8000
WORKDIR /opt/django-app
COPY . /opt/django-app/
RUN apt install -y default-libmysqlclient-dev
RUN pip install -r requirements.txt
EXPOSE $APP_PORT


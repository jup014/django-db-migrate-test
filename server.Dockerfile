FROM python:3.9

RUN apt update

ADD server /server
COPY server /server
WORKDIR /server
RUN pip install -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate

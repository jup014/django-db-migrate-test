FROM python:3.9
ENV PYTHONUNBUFFERED 1

ADD server /server
COPY server /server
WORKDIR /server

RUN apt-get update
RUN pip install -r requirements.txt
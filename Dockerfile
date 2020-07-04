FROM python:3.7-buster
MAINTAINER Todd Jacobus

RUN apt-get update
RUN apt-get --assume-yes install gdal-bin
RUN apt-get --assume-yes install libgeos-dev

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

# RUN adduser -D user
# USER user
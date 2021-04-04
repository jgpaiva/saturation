FROM python:3.9.3-slim

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY requirements.txt /opt/app

RUN pip install -r requirements.txt

COPY . /opt/app

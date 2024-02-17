FROM ubuntu:latest
LABEL authors="makarov"

WORKDIR /home/insurance_hakaton

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/home
ENV APP_HOME=/home/insurance_hakaton

#RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    libzbar0 \
    libgl1-mesa-glx \
    libglib2.0-0

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install datetime

COPY . .
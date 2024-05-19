FROM ubuntu:latest
LABEL authors="makarov"

WORKDIR /home/insurance_hakaton

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/makarov
ENV APP_HOME=/home/makarov/insurance

#RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    libzbar0 \
    libglib2.0-0 \
    libgl1 \
    libsm6 \
    libxext6 \
    libxrender1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Создаем виртуальную среду и активируем ее
RUN python3 -m venv $APP_HOME/venv
ENV PATH="$APP_HOME/venv/bin:$PATH"

# Устанавливаем зависимости в виртуальной среде
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install datetime
RUN pip install gunicorn


COPY . .
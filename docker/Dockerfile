FROM python:3.6-stretch
LABEL maintainer="PolySwarm Developers <info@polyswarm.io>"

ENV DOCKERIZE_VERSION v0.6.1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY pytest.ini setup.py README.md ./
COPY src src
COPY tests tests

RUN pip install /app
FROM python:3.10-alpine
RUN apk update \
  && apk add \
  build-base \
  postgresql \
  postgresql-dev \
  git \
  libpq

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
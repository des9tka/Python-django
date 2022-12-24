FROM python:3.11-alpine

MAINTAINER Some Dev

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache --virtual ..build-deps gss musl-dev mariadb-dev
#for Pillow
RUN apk add --no-cache --virtual jpeg-dev zlib-dev libjpeg

RUN mkdir /app
WORKDIR /app

RUN adduser -D user
RUN chown -R user:user /app
USER user

ENV PATH="/home/user/.local/bin:${PATH}"

COPY Pipfile /tmp

RUN cd /tmp\
    && pip install --upgrade pip\
    && pip intasll --userpipenv\
    && pipenv lock\
    && pipenv requirements > requirements.txt\
    && pip intall --user -r requirements.txt
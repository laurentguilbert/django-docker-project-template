FROM python:3.5
RUN apt-get update
RUN apt-get install gettext -y
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web
ADD . /web/
RUN python bootstrap.py && bin/buildout -c production.cfg
RUN bin/project collectstatic --noinput

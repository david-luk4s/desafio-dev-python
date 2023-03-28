FROM python:3.9-slim-buster

WORKDIR /usr/src/app

ADD requirements.txt ./requirements.txt
RUN  python -m pip install -U pip && pip install -r requirements.txt
COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["sh", "docker-entrypoint.sh"]
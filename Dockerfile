FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install -U pip
RUN pip install Flask

COPY ./app /app

ENV MESSAGE "Docker Success"
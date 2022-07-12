FROM python:3.10-slim-buster as builder
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/lib/python3.9/site-packages
RUN set -e;

RUN apt-get -y update
RUN apt-get -y install gcc libpq5 postgresql postgresql-contrib

ADD pyproject.toml poetry.lock ./

RUN python -m pip install -U pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

WORKDIR /opt/app

FROM builder AS application
RUN poetry install --no-dev
ADD . /opt/app/
ENTRYPOINT [ "./docker-entrypoint.sh" ]
CMD ["uwsgi", "--ini", "uwsgi.ini"]

FROM builder AS development
RUN poetry install
ADD . /opt/app
CMD ["python", "manage.py", "runserver", "0:8000"]


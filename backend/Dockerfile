FROM python:3.8.13-slim

ENV DATABASE_HOST=""
ENV DATABASE_PASSWORD=""
ENV DATABASE_USER=""
ENV DABABASE_SCHEMA=""


RUN pip3 install --no-cache-dir pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN set -ex && pipenv install --deploy --system

COPY ./app /app

WORKDIR /app

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
FROM python:3.7.3

RUN apt-get update && apt-get install -y gettext xmlsec1 && \
    pip install --upgrade pip poetry

WORKDIR /app

COPY pyproject.toml pyproject.toml

RUN poetry config settings.virtualenvs.create false && poetry install

COPY . /app

ENTRYPOINT ["/app/docker/entry"]
CMD ["runserver"]



FROM python:3.10-alpine

RUN apk update --no-cache && apk upgrade --no-cache --available

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml /code

RUN poetry install --without test

COPY src /code/src

EXPOSE 8000

CMD ["poetry", "run", "fastapi", "run"]


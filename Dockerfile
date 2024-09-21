FROM python:3.10-alpine

RUN apk  update --no-cache && apk upgrade --no-cache --available

WORKDIR /code

COPY pyproject.toml /code

RUN pip install poetry

RUN poetry install

COPY . /code

EXPOSE 8000

CMD ["poetry", "run", "fastapi", "run"]


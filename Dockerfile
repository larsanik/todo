FROM python:3.13.0-slim

RUN apt-get update && apt-get install -yq curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$PATH:$POETRY_HOME/bin"

# в контейнере делать виртуальные окружения нет смысла, так как на каждое приложение свой контейнер
# запрещаем poetry создавать виртуальное окружение
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY . .

RUN poetry install
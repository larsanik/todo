FROM python:3.13.0-slim

RUN pip install poetry

# в контейнере делать виртуальные окружения нет смысла, так как на каждое приложение свой контейнер
# запрещаем poetry создавать виртуальное окружение
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY . .

RUN poetry install
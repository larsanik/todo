ARG DEPS=prod

# для сборки docker build --target base-prod . -t dev
# после добавления ARG так docker build --build-arg DEPS=prod . -t dev
FROM python:3.13.0-slim AS base-prod

RUN apt-get update && apt-get install -yq curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$PATH:$POETRY_HOME/bin"

# в контейнере делать виртуальные окружения нет смысла, так как на каждое приложение свой контейнер
# запрещаем poetry создавать виртуальное окружение
RUN poetry config virtualenvs.create false \
    && poetry config cache-dir /cache/poetry
    # ^ добавили папку для хранения кеша зависимостей, чтобы не создавать при каждой сборке

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=/cache/poetry \
    poetry install --only main

# наследован от base-prod
# для сборки docker build --target base-dev . -t dev (в toml должен быть соотвесвующий раздел dev
# с зависимостями для разработки(тестирование и т.д.). В моем проекте такого нет, поэтому ошибка при сборке.)
# после добавления ARG так docker build --build-arg DEPS=dev . -t dev
FROM base-prod AS base-dev

RUN --mount=type=cache,target=/cache/poetry \
    poetry install --only dev

# для исключения дублирования в стейджах сборки прода или разработки
FROM base-${DEPS} AS final

COPY . .

RUN poetry install --only-root

# настройка точки запуска программы
ENTRYPOINT ["bash", "-c"]
CMD ["./docker-entrypoint.sh"]

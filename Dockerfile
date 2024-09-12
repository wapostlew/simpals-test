FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential libssl-dev libffi-dev\
    python3-dev \
    && rm -rf /var/lib/apt/list*

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-root

EXPOSE ${EXPOSE_PORT}

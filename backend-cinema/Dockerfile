FROM python:3.13.5-bullseye

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        libgl1 \
        curl \
    && rm -rf /var/lib/apt/lists/*

COPY backend-cinema/requirements.txt .
COPY .env .
COPY backend-cinema/docker-entrypoint.sh .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend-cinema/src/ ./src/

ENV PYTHONPATH=/app/src

EXPOSE 8000

CMD ["sh", "docker-entrypoint.sh"]

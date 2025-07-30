FROM python:3.13.5-bullseye

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        curl \
    && rm -rf /var/lib/apt/lists/*

COPY backend-cinema/requirements.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend-cinema/src/ ./src/

COPY backend-cinema/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENV PYTHONPATH=/app/src

EXPOSE 8000

CMD ["/docker-entrypoint.sh"]

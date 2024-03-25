FROM python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN make install
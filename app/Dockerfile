# ---------- Stage 1: Builder ----------
FROM python:3.10-alpine AS builder

WORKDIR /app

RUN apk add --no-cache build-base

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.10-alpine

WORKDIR /app

RUN adduser -D appuser

# Install curl for healthcheck
RUN apk add --no-cache curl

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Remove pip, setuptools, wheel
RUN rm -rf /usr/local/lib/python3.10/site-packages/pip* \
           /usr/local/lib/python3.10/site-packages/setuptools* \
           /usr/local/lib/python3.10/site-packages/wheel*

COPY app.py .

USER appuser

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]


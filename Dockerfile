FROM python:3.12-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

RUN flake8 src/dogs_api --max-line-length=119 --exclude=src/dogs_api/migrations

RUN chmod +x entrypoint.sh

CMD ["/bin/sh", "entrypoint.sh"]

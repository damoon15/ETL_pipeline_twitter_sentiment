FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "etl.py"]

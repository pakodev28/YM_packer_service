FROM python:3.13.0a3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000"]

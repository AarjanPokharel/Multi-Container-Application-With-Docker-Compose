FROM python:3

WORKDIR /app

COPY src/requirements.txt /app

RUN pip install -r requirements.txt

COPY src/* /app

COPY static /app/static

COPY templates /app/templates

CMD [ "python", "app.py" ]


FROM python:3.9-alpine AS base

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

FROM python:3.9-alpine
COPY --from=base /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

RUN mkdir /app
WORKDIR /app

COPY . /app/

CMD ["ls -la /app"]

CMD ["python", "main.py"]
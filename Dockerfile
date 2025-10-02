FROM python:3.9

WORKDIR /code

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

COPY ./app/wait-for-it.sh /code/app/wait-for-it.sh
RUN chmod +x /code/app/wait-for-it.sh

ENV PYTHONPATH=/code

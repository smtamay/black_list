#!/bin/bash

/code/app/wait-for-it.sh db:5432 -t 30 -- echo "PostgreSQL está listo"

python /code/app/db/init_db.py
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

FROM python:3.13.2

WORKDIR /main

COPY . .

RUN poetry install --no-root



CMD ["python","main.py"]
FROM python:3.9-slim-buster

WORKDIR /app

COPY portchecker.py portchecker.py

CMD [ "python3", "portchecker.py"]
# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /backup
COPY . .
RUN apt-get update -y
RUN apt-get install mariadb-client -y
RUN pip install -r requirements.txt
CMD ["python", "periodic_healthcheck.py", "86400"] # every day
EXPOSE 8002

FROM ubuntu:latest
FROM python:3.9
EXPOSE 8080
LABEL authors="Stephen"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/*

CMD ["python", "app.py"]
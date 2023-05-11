FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

RUN cd /app

ENTRYPOINT ["sh", "docker-entrypoint.sh"]
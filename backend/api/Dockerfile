FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

RUN cd /app

RUN python manage.py collectstatic --no-input -v 2
#RUN python manage.py migrate --noinput
#RUN python manage.py createsuperuser --noinput --username "$DJANGO_USERNAME"
CMD ["gunicorn", "-c", "config/gunicorn/production.py"]
FROM python:3

COPY . /work

WORKDIR /work

EXPOSE 80

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD gunicorn --workers 2 --bind 0.0.0.0:80 blog:blog
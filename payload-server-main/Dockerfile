FROM python:3.9-alpine

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY payload-server.py .

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "payload-server:app"]
EXPOSE 5000

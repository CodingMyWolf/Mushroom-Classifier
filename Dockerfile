FROM python:3

WORKDIR MCapp/app/backend
COPY . /MCapp

EXPOSE 8080

RUN pip install -r ../../requirements.txt

CMD ["python3", "server.py"]


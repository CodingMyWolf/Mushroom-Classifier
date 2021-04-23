FROM python:3

WORKDIR MCapp 
COPY . /MCapp

EXPOSE 8080

RUN pip install -r requirements.txt

CMD ["python3", "app/backend/server.py"]


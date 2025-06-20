FROM python:3.10

RUN mkdir /app

WORKDIR /app

ADD .. .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "run.py"]

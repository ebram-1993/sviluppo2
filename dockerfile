FROM python:3.12.10


WORKDIR /app


COPY . /app

RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py"]
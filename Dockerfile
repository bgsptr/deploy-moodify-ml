FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install tensorflow

ENV PORT 8080
EXPOSE ${PORT}

CMD ["python", "app.py"]
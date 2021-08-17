FROM python:3.7-alpine
WORKDIR /app
ADD . /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]
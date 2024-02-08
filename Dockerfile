FROM python:3.9-alpine
WORKDIR /usr/src/app
COPY . .


RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/usr/src/app

CMD ["python", "app/__init__.py"]

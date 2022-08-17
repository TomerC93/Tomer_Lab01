FROM python:3.8-slim as serve
WORKDIR /usr/src/app
RUN     pip install -r requirements.txt 
COPY . .
CMD ["python", "app.py"]

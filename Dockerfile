FROM python:3.8-slim
WORKDIR /usr/src/app
COPY . .
RUN    mkdir /home/${USER}/.aws && \
       mv config /home/${USER}/.aws && \
       mv credentials /home/${USER}/.aws && \ 
       pip install -r requirements.txt 
CMD ["python", "app.py"]

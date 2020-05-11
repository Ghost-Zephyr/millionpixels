FROM python:3.8-slim-buster

RUN apt -y update && apt -y upgrade &&\
 pip3 install --upgrade pip &&\
 mkdir /opt/app

COPY . /opt/app
WORKDIR /opt/app

RUN pip3 install -r requirements.txt

CMD [ "gunicorn", "server:app", "-b", "0.0.0.0:8000", "-w", "1", "--threads", "4" ]

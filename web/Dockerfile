# used ubuntu as there was issue using python:3.6 image

FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y  python3-pip python3-dev 

COPY . /

RUN pip3 install -r requirements.txt && pip3 install gunicorn

# echo "download Imagenet model for future use"
RUN python3 download_model.py

ENTRYPOINT ["/runserver.sh"]

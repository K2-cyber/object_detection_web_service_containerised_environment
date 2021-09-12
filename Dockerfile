# Base image
FROM ubuntu
FROM python
#MAINTAINER <Kapish Kuchroo 31213294 kkuc0001@student.monash.edu>
WORKDIR /usr/src/app

COPY . .
RUN apt-get update -y && apt-get install -y python3-pip python3-dev libsm6 libxext6 libxrender-dev
RUN apt install libgl1-mesa-glx -y
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
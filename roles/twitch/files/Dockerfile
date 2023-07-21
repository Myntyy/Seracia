FROM python:3.8-slim
RUN apt update && apt install python3-pip -y
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY twitch.py
CMD python3 twitch.py
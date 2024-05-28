FROM python:3.12-slim
LABEL maintainer="sma4no.7@gmail.com"
ENV PYTHONUNBUFFERED=1
WORKDIR app/
COPY requirements.txt ./
RUN pip install -r requirements.txt

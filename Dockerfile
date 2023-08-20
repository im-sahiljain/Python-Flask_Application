FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    vim \
    python3 \
    python3-pip

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]


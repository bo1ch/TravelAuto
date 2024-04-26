FROM python:3.11.4

ARG run_env
ENV env $ run_env

WORKDIR ./TravelAuto

COPY . .

RUN apt-get update && apt-get install -y bash && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

RUN pip3 install -r requirements.txt

CMD pytest -s -v tests/*
#WORKDIR /app
#
#COPY . /app
#
#RUN pip install --trusted-host pypi.python.org -r requirements.txt
#
#RUN apt-get update && apt-get install -y wget unzip && \
#    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
#    apt install -y ./google-chrome-stable_current_amd64.deb && \
#    rm google-chrome-stable_current_amd64.deb && \
#    apt-get clean
#
#CMD ["python", "main.py"]
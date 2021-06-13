# 任意のイメージを取得
FROM python:3.10-rc-slim-buster

RUN apt -y update && apt -y upgrade
RUN apt install -y g++ gcc 

RUN pip install pycld2

# RUN apt update && apt upgrade
# RUN apt install git
# 
# WORKDIR /tmp
# RUN git clone http://github.com/abosamoor/pycld2.git
# RUN cd pycld2
# RUN python3 ./setup.py install

WORKDIR /opt/app

COPY app /opt/app

RUN chmod 755 /opt/app/start.sh

RUN python --version

CMD [ "/opt/app/start.sh" ]

FROM python:3.12-slim

RUN apt-get update && apt-get install -y gcc g++ libatlas-base-dev libffi-dev libbz2-dev libssl-dev liblzma-dev libsqlite3-dev

RUN pip install --no-cache-dir paho-mqtt numpy scipy scikit-fuzzy

COPY run.sh /run.sh
COPY fuzzy_service.py /fuzzy_service.py
RUN chmod +x /run.sh

CMD [ "/run.sh" ]

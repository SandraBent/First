FROM python:3.9
WORKDIR /

RUN pip install flask
RUN pip install google-cloud-datastore

COPY . .
CMD [ "python3", "app.py" ]

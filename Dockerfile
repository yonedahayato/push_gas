FROM python:3.6-slim

RUN pip install \
  requests \
  tornado

WORKDIR /push_line

ADD . .

CMD python recieve_message.py

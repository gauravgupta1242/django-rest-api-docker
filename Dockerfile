FROM python:3

ENV PORT=8000
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt


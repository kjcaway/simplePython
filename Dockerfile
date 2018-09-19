FROM python:3
MAINTAINER www.github.com/kjcaway

RUN pip install Flask
RUN pip install pymongo

COPY . /app/

WORKDIR /app/src/

CMD python run.py
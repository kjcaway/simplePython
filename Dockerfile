FROM python:3
MAINTAINER www.github.com/kjcaway

RUN pip install Flask
RUN pip install pymongo
RUN pip install datetime
RUN pip install Flask-Babel
RUN pip install mongoengine
RUN pip install cuid

COPY . /app/

WORKDIR /app/

CMD sh cmd.sh

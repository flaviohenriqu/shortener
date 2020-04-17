FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
RUN mkdir /app
WORKDIR /app
ADD Pipfile /app/
RUN pipenv install
ADD . /app/

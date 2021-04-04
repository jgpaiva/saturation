FROM ruby:3.0.0-slim

RUN apt-get update && apt-get install -y build-essential

RUN mkdir -p /app
WORKDIR /app
COPY Gemfile /app
COPY Gemfile.lock /app

RUN bundle install

COPY . /app

CMD puma -t 10:10 -w 1 -p 8080
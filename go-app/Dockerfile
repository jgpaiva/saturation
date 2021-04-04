FROM golang:1.16.3-alpine

RUN mkdir -p /app
WORKDIR /app
COPY . /app

RUN go build

CMD ./app
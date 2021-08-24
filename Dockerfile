ARG env

FROM dockerhub.ir/ubuntu:20.04 AS base
RUN apt-get update 
RUN apt-get install -y python3-pip
ADD . /app
WORKDIR /app

FROM base as env-production
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS env-test
RUN pip install --no-cache-dir -r requirements.txt -r requirements-devel.txt

FROM env-${env} AS final
EXPOSE 8080
CMD ["./docker-entrypoint.sh"]
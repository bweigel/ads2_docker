#!/usr/bin/env bash

CONTAINER="airflow"

docker rm -f ${CONTAINER}
docker run -ti --name ${CONTAINER} \
-v $(pwd)/mnt:/workd -p 8080:8080 bweigel/airflow:latest
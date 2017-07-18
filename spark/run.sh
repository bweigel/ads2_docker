#!/usr/bin/env bash

CONTAINER="spark"

docker rm -f ${CONTAINER}
docker run -ti \
  --expose 7001-7006 \
  -p 4050:4040 \
  -p 7077:7077 \
  -p 8090:8080 \
  -p 6066:6066 \
  --user spark \
  --name ${CONTAINER} \
 -v $(pwd)/mnt:/workd \
bweigel/spark:latest
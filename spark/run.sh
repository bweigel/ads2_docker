#!/usr/bin/env bash

CONTAINER="spark"

docker rm -f ${CONTAINER}
docker run -ti --name ${CONTAINER} \
 -v $(pwd)/mnt:/workd \
bweigel/spark:latest
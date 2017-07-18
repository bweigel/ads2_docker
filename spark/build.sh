#!/usr/bin/env bash

IMAGE="spark"

docker images | grep $IMAGE | awk '{print $3}' | xargs docker rmi -f
docker build -t bweigel/${IMAGE}:latest  .
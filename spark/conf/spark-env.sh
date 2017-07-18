#!/usr/bin/env bash


export SPARK_DIST_CLASSPATH=$(/opt/hadoop/bin/hadoop classpath):/opt/hadoop/share/hadoop/tools/lib/*:/opt/hadoop/share/hadoop/tools/*
export SPARK_MASTER_PORT=7077
export SPARK_MASTER_WEBUI_PORT=8080
export SPARK_PUBLIC_DNS=127.0.0.1
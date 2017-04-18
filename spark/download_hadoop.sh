#!/bin/sh

MIRROR=$(curl --stderr /dev/null https://www.apache.org/dyn/closer.cgi\?as_json\=1 | jq -r '.preferred')
FILENAME="hadoop-${HADOOP_VERSION}.tar.gz"
URL="${MIRROR}hadoop/common/hadoop-${HADOOP_VERSION}/${FILENAME}"

OUTPUT="/tmp/${FILENAME}"

echo "downloading ${URL}..."
wget -q "${URL}" -O "${OUTPUT}"
tar xfz "${OUTPUT}" -C /opt

EXTRACTED_NAME=$(tar tfz "${OUTPUT}" | head -n 1  | tr "/" "\n" | head -n 1)
ln -s /opt/${EXTRACTED_NAME}/. /opt/hadoop

rm "${OUTPUT}"

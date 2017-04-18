#!/bin/sh

FILENAME="Miniconda3-latest-Linux-x86_64.sh"
URL="https://repo.continuum.io/miniconda/${FILENAME}"
OUTPUT="/tmp/${FILENAME}"

echo "downloading ${URL}..."
wget -q "${URL}" -O "${OUTPUT}"
chmod a+x ${OUTPUT}
${OUTPUT} -b
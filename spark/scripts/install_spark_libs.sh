#!/usr/bin/env bash

mkdir /opt/spark_libs

pushd .

cd /opt
git clone https://github.com/graphframes/graphframes.git
mv graphframes/python /opt/spark_libs/.
rm -rf graphframes

cd /opt/spark_libs
wget https://s3.amazonaws.com/redshift-downloads/drivers/RedshiftJDBC42-1.2.1.1001.jar
popd

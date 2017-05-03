FROM anapsix/alpine-java

ARG spark_version=2.1.0
ARG scala_version=2.11
ARG hadoop_version=2.8.0

RUN apk add --update unzip wget curl docker jq coreutils python3
RUN ln -s /usr/bin/python3 /usr/bin/python

ENV SPARK_VERSION=$spark_version 
ENV HADOOP_VERSION=$hadoop_version

ADD download_spark.sh /tmp/.
ADD download_hadoop.sh /tmp/.
ADD download_all.sh /tmp/.

RUN chmod a+x /tmp/download_all.sh && sync && /tmp/download_all.sh 

# VOLUME ["/spark"]

ENV HADOOP_HOME /opt/hadoop/
ENV HADOOP_CONF_DIR ${HADOOP_HOME}/conf
ENV SPARK_HOME /opt/spark
ENV PATH ${PATH}:${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${HADOOP_HOME}/bin
ADD conf/spark-defaults.conf ${SPARK_HOME}/conf/spark-defaults.conf
ADD conf/spark-env.sh ${SPARK_HOME}/conf/spark-env.sh

# The scripts need to have executable permission
RUN chmod a+x ${SPARK_HOME}/conf/spark-env.sh
# Use "exec" form so that it runs as PID 1 (useful for graceful shutdown)
#CMD ["start-master.sh"]

CMD ["/bin/bash"]

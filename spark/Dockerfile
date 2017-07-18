FROM anapsix/alpine-java

ARG spark_version=2.1.1
ARG scala_version=2.11
ARG hadoop_version=2.8.0

RUN apk add --update unzip wget curl docker jq coreutils python3 procps
RUN ln -s /usr/bin/python3 /usr/bin/python

ENV SPARK_VERSION=$spark_version
ENV HADOOP_VERSION=$hadoop_version
#ENV SPARK_MASTER_LOG=/mnt/spark/logs

COPY scripts/* /tmp/

# Run all scripts inside scripts folder
RUN chmod a+x /tmp/run_all.sh && sync && /tmp/run_all.sh

ENV HADOOP_HOME /opt/hadoop/
ENV HADOOP_CONF_DIR ${HADOOP_HOME}/conf

ENV SPARK_HOME /opt/spark
ENV PYSPARK_PYTHON /usr/bin/python3
ENV PATH ${PATH}:${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${HADOOP_HOME}/bin
ADD conf/* ${SPARK_HOME}/conf/

ENV PYTHONPATH "$PYTHONPATH:/opt/spark_libs/graphframes/python"
RUN echo "spark.jars.packages=graphframes:graphframes:0.5.0-spark$(echo $SPARK_VERSION | grep -Eo "[0-9]\.[0-9]")-s_2.11" >> $SPARK_HOME/conf/spark-defaults.conf

# The scripts need to have executable permission
RUN chmod a+x ${SPARK_HOME}/conf/spark-env.sh

RUN adduser -Ds /bin/bash -h /home/spark -u 1000 spark

EXPOSE 4040 6066 7077 8080

RUN chown spark. /opt/ -R
USER spark
WORKDIR /home/spark

# Use "exec" form so that it runs as PID 1 (useful for graceful shutdown)
#CMD ["start-master.sh"]

CMD ["/bin/bash"]

FROM python:3.6.0-alpine

ARG AIRFLOW_VERSION=1.8.0
ARG AIRFLOW_HOME=/usr/local/airflow

RUN apk add --no-cache --virtual .build-deps \
        bash gcc libxml2-dev libxslt-dev linux-headers musl-dev \
        python-dev \
        libffi-dev \
        openssl-dev \
        postgresql-dev \
        krb5-dev \
        libgsasl-dev \
        build-base \
        git

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip install virtualenv \
  && rm -rf /var/cache/apk/*

RUN pip install -U pip \
    && pip install Cython \
    && pip install pytz \
    && pip install pyOpenSSL \
    && pip install ndg-httpsclient \
    && pip install pyasn1
RUN pip install airflow[crypto,celery,postgres,hive,s3,jdbc]==$AIRFLOW_VERSION \
    && pip install celery[redis]==3.1.17 \
    && rm -rf \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base

RUN apk update && apk add --no-cache bash bash-completion
RUN adduser -s /bin/bash -h ${AIRFLOW_HOME} -D airflow
#RUN apk del .build-deps

COPY mnt/airflow.cfg ${AIRFLOW_HOME}/.
COPY mnt/entrypoint.sh /usr/bin/.

RUN mkdir /workd
RUN chown -R airflow /workd
RUN chown -R airflow ${AIRFLOW_HOME}

RUN chmod +x /usr/bin/entrypoint.sh

EXPOSE 8080  5555 8793

USER airflow
WORKDIR ${AIRFLOW_HOME}
ENV AIRFLOW_HOME=${AIRFLOW_HOME}

CMD ["/bin/bash"]

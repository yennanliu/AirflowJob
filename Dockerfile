FROM astronomerinc/ap-airflow:0.7.5-1.10.1-onbuild

ENV HOME /app
WORKDIR $HOME
COPY . $HOME

RUN /bin/bash -c "source install_pyspark.sh"


#https://github.com/astronomerio-archive/docker-airflow/blob/master/Dockerfile
#ENV PYTHONPATH ${PYTHONPATH}:${AIRFLOW_HOME}
#ENV PYTHONPATH ${PYTHONPATH}:${pwd}
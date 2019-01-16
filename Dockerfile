# stage 0)
FROM astronomerinc/ap-airflow:0.7.5-1.10.1-onbuild AS base

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Set up env var
ENV HOME /app
ENV SPARK_HOME /spark
WORKDIR $HOME
COPY . $HOME

# install spark 
RUN /bin/bash -c "source install_pyspark.sh"


# stage 1)
FROM java:8-jdk AS java_layer 

# Set up env var
ENV HOME /app
ENV SPARK_HOME /spark
WORKDIR $HOME
COPY . $HOME

# stage 2)
# merge stage 0 and stage 1 
FROM base 
COPY --from=java_layer /app /app


# ----------------------- dev -----------------------
#https://github.com/astronomerio-archive/docker-airflow/blob/master/Dockerfile
#ENV PYTHONPATH ${PYTHONPATH}:${AIRFLOW_HOME}
#ENV PYTHONPATH ${PYTHONPATH}:${pwd}
# ----------------------- dev -----------------------

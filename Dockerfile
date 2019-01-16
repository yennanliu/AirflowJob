
# stage 0)
FROM ubuntu AS stage_0 
RUN yes Y |  apt-get update &&  yes Y | apt-get install git
# Install Java
RUN yes Y | apt-get update \
    && yes Y | apt-get install --no-install-recommends -y openjdk-8-jre-headless \
    && rm -rf /var/lib/apt/lists/*


# Set up env var
ENV HOME /java
ENV SPARK_HOME /spark
WORKDIR $HOME
COPY . $HOME


# stage 1)
FROM astronomerinc/ap-airflow:0.7.5-1.10.1-onbuild AS stage_1

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

COPY --from=stage_0 . $HOME


# install spark 
#RUN /bin/bash -c "source install_pyspark.sh"


# stage 2)
# merge stage 0 and stage 1 
FROM stage_1 as stage_FINAL  

EXPOSE 8080


# ----------------------- dev -----------------------
#https://github.com/astronomerio-archive/docker-airflow/blob/master/Dockerfile
#ENV PYTHONPATH ${PYTHONPATH}:${AIRFLOW_HOME}
#ENV PYTHONPATH ${PYTHONPATH}:${pwd}
# ----------------------- dev -----------------------

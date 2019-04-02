# stage 0)
FROM astronomerinc/ap-airflow:0.7.5-1.10.1-onbuild AS stage_0 

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Set up env var
ENV HOME /
ENV SPARK_HOME /spark
WORKDIR $HOME
COPY . $HOME

# Install Java
RUN apk update && apk add git
RUN apk add openjdk8

# Install Spark 
RUN /bin/bash -c "source install_pyspark.sh"

# Install scikit-learn
#RUN pip install --upgrade scikit-learn

# Expose port 8000
EXPOSE 8080

# ----------------------- dev -----------------------
#https://github.com/astronomerio-archive/docker-airflow/blob/master/Dockerfile
#ENV PYTHONPATH ${PYTHONPATH}:${AIRFLOW_HOME}
#ENV PYTHONPATH ${PYTHONPATH}:${pwd}
# ----------------------- dev -----------------------
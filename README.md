# XBot
- Auto routine jobs and push to slack channel 
- Managed by Airflow pipeline 
- Instagram, SPARK, ML jobs  

## Tech 
- python 3 
- Astro Airflow 
- InstaPy
- Docker 

## File structure

```bash
# .
# ├── Dockerfile             : Dockerfile define astro airflow env 
# ├── Dockerfile_dev         : Dockerfile dev file 
# ├── README.md
# ├── airflow_quick_start.sh : commands help start airflow 
# ├── clean_airflow_log.sh   : clean airflow job log / config before reboost airflow
# ├── dags                   : airflow job main scripts 
# ├── ig                     : IG job scripts 
# ├── install_pyspark.sh     : script help install pyspark local 
# ├── packages.txt           : packages for astro airflow in system level 
# ├── plugins                : plugins help run airflow jobs 
# ├── populate_creds.py      : script help populate credential (.creds.yml) to airflow 
# ├── requirements.txt       : packages for astro airflow in python  level 
# ├── .creds.yml             : yml save creds access services (slack/s3/...) 

```


## Quick Start (Airflow)

```bash
# STEP 0) install env 
git clone https://github.com/yennanliu/XBot && cd XBot
bash install_pyspark.sh 
# STEP 1) run the dev env and export SPARK_HOME
source activate pyspark_
export SPARK_HOME=/Users/$USER/spark
export PATH=$SPARK_HOME/bin:$PATH

# STEP 2) export AIRFLOW_HOME and set language as US.UTF-8 
export AIRFLOW_HOME=/Users/$USER/XBot
export PYTHONPATH=/Users/$USER/XBot
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
# STEP 3) init airflow webserver
### in the current termianl ###
airflow initdb
airflow webserver -p 8088

# STEP 4) init airflow scheduler
### OPEN UP THE OTHER NEW TERMINAL, RUN STEP 1) -> STEP 2), THEN RUN FOLLOWING COMMAND ### 
airflow scheduler
# STEP 5) access airflow UI
# http://localhost:8088
```


### Quick Start (Astronomer Airflow)

```bash

# https://www.astronomer.io/docs/getting-started/

# STEP 0) INSTALL PYTHON ENVIRONMENT

# set up dev environment 
conda update conda && conda create -n XBot_dev python=3.5 
# launch dev env 
source activate XBot_dev
# install needed packages (python)
pip install -r requirements.txt
# install InstaPy
# https://github.com/timgrossmann/InstaPy#basic-installation
pip install git+https://github.com/timgrossmann/InstaPy.git

# STEP 1)  INSTALL ASTRO AIRFLOW 

# Install go 
brew install go
# get astronomer CLI
curl -sL https://install.astronomer.io | sudo bash
# verify install success 
astro 
# init airflow 
cd && cd XBot && astro airflow init 

# TODO : populate crendentials (DB/S3...)

# STEP 2) RUN ASTRO AIRFLOW LOCAL 

# Run the Astro Airflow locally 
# make sure the Docker daemon APP is alrady runnning 
astro airflow start
# check astro docker status 
docker ps
# check docker log 
docker logs $(docker ps | grep scheduler | awk '{print $1}')

############## PART 4 : KILL/REBOOST ASTRO AIRFLOW ##############
# kill airflow 
astro airflow kill
# re-boost airflow 
astro airflow init
astro airflow start

# STEP 3): INTEGRATE WITH SLACK 

# set up Slack bot app 
# https://api.slack.com/apps
# test with setting 
curl -X POST -H 'Content-type: application/json' --data '{"text":" 12345"}' https://hooks.slack.com/services/<ur_workspace_id>/<ur_channel_id>/<ur_access_token>

```

## Docker Deploy 
- dev 

## CI/CD 
- Travis CI 

## Development 
- dev 



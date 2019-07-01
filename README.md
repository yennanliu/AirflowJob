# XJob

[![Build Status](https://travis-ci.org/yennanliu/Xjob.svg?branch=master)](https://travis-ci.org/yennanliu/Xjob)
[![PRs](https://img.shields.io/badge/PRs-welcome-6574cd.svg)](https://github.com/yennanliu/Xjob/pulls)

> As `ETL build` part of the "Daas (Data as a service) repo", we demo how to build a ETL system running for data engineering/science via Airflow in this POC project. Main focus:  1) ETL/ELT (extract, transform, load) env setting up 2) ETL code base development 3) ETL code test 4) 3rd party API intergration (Instagram, Slack..) 4) dev-op tools (Travis CI). 

* Daas (Data as a service) repo :  [Data infra build](https://github.com/yennanliu/data_infra_repo) -> [ETL build](https://github.com/yennanliu/XJob) -> [DS application demo](https://github.com/yennanliu/analysis)
* Airflow Heroku demo : [airflow-heroku-dev](https://github.com/yennanliu/airflow-heroku-dev)

## Tech 
```bash 
- Programming : Python 3, Java, Shell 
- Framework   : Airflow, Spark, InstaPy, scikit-learn, Keras 
- dev-op      : Docker, Travis  
```

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

## Installation 

### STEP 1) Prerequisites
- Copy [.creds.yml.dev](https://github.com/yennanliu/Xjob/blob/master/.creds.yml.dev) as `.creds.yml` file then input your credential in it.
- Please have a look on [Airflow documentation](https://airflow.apache.org/) before start

### STEP 2') Quick Start ( via `Airflow`)
- [Airflow quick start](https://github.com/yennanliu/Xjob/blob/master/doc/airflow_quick_start.md)

### STEP 2'') Quick Start (via `Astronomer Airflow`)
- There is an issue when run Spark job via Astro airflow, feel free to leave a [ PR ](https://github.com/yennanliu/Xjob/pulls)for that 🙏
- [Astro Airflow quick start ](https://github.com/yennanliu/Xjob/blob/master/doc/astro_airflow_quick_start.md)

## Development 

### Docker image 
- [Docker hub](https://cloud.docker.com/u/yennanliu/repository/docker/yennanliu/xjob_env_instance)

### CI/CD 
- [Travis](https://travis-ci.org/yennanliu/Xjob/builds)

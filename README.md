# XBot
- Auto daily jobs and push to slack channel 
- Managed by Airflow pipeline 
- //dev 


# Tech 
- python 3 
- Astro Airflow 
- InstaPy
- Docker 

# File structure
```bash
#├── Dockerfile
#├── README.md
#├── dags
#│   └── example-dag.py
#├── include
#├── packages.txt
#├── plugins
#│   └── example-plugin.py
#└── requirements.txt

```


# Quick Start ( Run Airflow via Astronomer local)

```bash

# https://www.astronomer.io/docs/getting-started/

############## PART 1 : INSTALL PYTHON ENVIRONMENT  ##############

# set up dev environment 
conda update conda && conda create -n XBot_dev python=3.5 
# launch dev env 
source activate XBot_dev
# install needed packages (python)
pip install -r requirements.txt
# install InstaPy
# https://github.com/timgrossmann/InstaPy#basic-installation
pip install git+https://github.com/timgrossmann/InstaPy.git

############## PART 2 : INSTALL ASTRO AIRFLOW  ##############

# Install go 
brew install go
# get astronomer CLI
curl -sL https://install.astronomer.io | sudo bash
# verify install success 
astro 
# init airflow 
cd && cd XBot && astro airflow init 

# TODO : populate crendentials (DB/S3...)

############## PART 3 : RUN ASTRO AIRFLOW LOCAL ##############

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

```

# Docker Deploy 

```bash 

# dev 

```

# CI/CD 
```bash

#dev 

```




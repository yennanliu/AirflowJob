### Quick Start (Astro Airflow) : dev 

- Currently these processes run OK, but have issues when trigger Spark job (via astro airflow docker). Please leave a PR if there is an idea, will be very appreciated that.   
- Access the UI : http://localhost:8088 


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

# STEP 3): KILL/REBOOST ASTRO AIRFLOW 
# kill airflow 
astro airflow kill
# re-boost airflow 
astro airflow init
astro airflow start

# STEP 4): INTEGRATE WITH SLACK 
# set up Slack bot app 
# https://api.slack.com/apps
# test with setting 
curl -X POST -H 'Content-type: application/json' --data '{"text":" 12345"}' https://hooks.slack.com/services/<ur_workspace_id>/<ur_channel_id>/<ur_access_token>
```
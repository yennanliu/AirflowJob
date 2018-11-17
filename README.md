# XBot
// Auto daily jobs and push to slack channel 
// Managed by Airflow pipeline 
// dev 




# Quick Start ( Run Airflow via Astronomer locally)

```bash

# https://www.astronomer.io/docs/getting-started/

# set up dev environment 
conda update conda && conda create -n XBot_dev python=3.5 

# launch dev env 
source activate XBot_dev



# install needed packages (python)
pip install -r requirements.txt

# install InstaPy
# https://github.com/timgrossmann/InstaPy#basic-installation
pip install git+https://github.com/timgrossmann/InstaPy.git

# Install go 
brew install go

# get astronomer CLI
curl -sL https://install.astronomer.io | sudo bash

# verify install success 
astro 

# init airflow 
astro airflow init 

# TODO : populate crendentials (DB/S3...)

# check astro docker status 
docker ps

# check docker log 
docker logs $(docker ps | grep scheduler | awk '{print $1}')

```

# Docker Deploy 

```bash 

# dev 

```





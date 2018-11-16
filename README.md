# XBot
// Auto daily jobs and push to slack channel 
// Managed by Airflow pipeline 
// dev 




# Quick Start ( Run Airflow via Astronomer locally)

```bash

# https://www.astronomer.io/docs/getting-started/

# Install go 
brew install go
# get astronomer CLI
curl -sSL https://install.astronomer.io | sudo bash

# install needed packages (python)
pip install -r requirements.txt

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





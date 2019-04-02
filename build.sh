#!/bin/sh

#################################################################
# SHELL SCRIPT BUILD DOCKER INSTANCE FOR TRAVIS CI   
#################################################################

echo ' ---------------- BUILD ALL REPO DOCKER IMAGES ----------------'
echo REGISTRY_USER = $REGISTRY_USER && echo REGISTRY_PASS = $REGISTRY_PASS

docker_images = ('Dockerfile')
for docker_images in "${docker_images[@]}"; 
	do 
		echo 'docker bulid : $docker_images .... ' && docker build . -t xbot_env_instance
	done 
# run test 
docker run -it Xbot_env_instance echo 'docker test 123'

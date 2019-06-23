#!/bin/sh
#################################################################
# SHELL TRIGGER WHOLE AIRFLOW TEST   
#################################################################

# declare env 
export AIRFLOW_HOME=/Users/$USER/XJob
export PYTHONPATH=/Users/$USER/XJob
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# init db (for airflow parameters (saved in DB))
airflow initdb

#lunch test 
pytest -m test 
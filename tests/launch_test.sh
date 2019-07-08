#!/bin/sh
#################################################################
# SHELL TRIGGER WHOLE AIRFLOW TEST   
#################################################################

# declare env 
export AIRFLOW_HOME=$(pwd)
export PYTHONPATH=$(pwd)
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# init db (for airflow parameters (saved in DB))
airflow initdb

# print file structure 
ls && pwd &&  echo 'AIRFLOW_HOME :' $AIRFLOW_HOME && echo 'PYTHONPATH :' $PYTHONPATH

#lunch test 
#pytest 
(echo 'run test via pytest.. ' && pytest -v tests/) || (echo 'run test via python.. ' && for i in $(echo $(ls tests/*_test.py) | cut -d' ' -f1-) ; do echo $i ; python $i ; done ) 
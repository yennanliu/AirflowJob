#!/bin/sh

if [[ -f "airflow.db" ]]; then 

	echo 'airflow.db exists'
	echo 'GET job list -------------- '
	sqlite3  airflow.db "select * from job;"
	echo 'GET dag list -------------- '
	sqlite3  airflow.db "select * from dag;"
else 
	echo 'airflow.db  NOT exists'
fi 
#!/bin/sh

echo 'GET job list -------------- '
sqlite3  airflow.db "select * from job;"
echo 'GET dag list -------------- '
sqlite3  airflow.db "select * from dag;"
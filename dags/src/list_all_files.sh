#!/bin/sh

#for file in $1/* ;  do     # root directory
for file in $(pwd)/* ;  do  # current directory
	echo $file 
	done   
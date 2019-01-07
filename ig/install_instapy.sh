#!/bin/sh
# https://github.com/timgrossmann/InstaPy

#################################################################
# SHELL HELP INSTALL INSTAPY ENV   
#################################################################


# 1) install dev env 
yes Y | conda create -n instapy python=3.6
source activate instapy
# 2) pull package 
pip install git+https://github.com/timgrossmann/InstaPy.git
# 3) install chrome driver 
# Download chromedriver for your system from here. Extract the .zip file and put it in /assets folder.
# chromedriver : https://sites.google.com/a/chromium.org/chromedriver/downloads
# file location :  /Users/yennanliu/anaconda3/lib/python3.6/site-packages/assets
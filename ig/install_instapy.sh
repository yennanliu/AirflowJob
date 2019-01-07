#!/bin/sh
# https://github.com/timgrossmann/InstaPy

#################################################################
# SHELL HELP INSTALL INSTAPY ENV   
#################################################################



yes Y | conda create -n instapy python=3.6
source activate instapy
pip install git+https://github.com/timgrossmann/InstaPy.git
#!/bin/sh
# https://blog.sicara.com/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f

#################################################################
# SCRIPT HELP INSTALL PYSPARK   
#################################################################
<<COMMENT1
#-------------------
Process : 
1) download spark bin-hadoop main file  (make sure you have Java 8 or newer version) 
2) unzip its and move to the ops location (default as /Users/yennanliu/spark )
3) copy all files under /Users/yennanliu/spark-2.3.0-bin-hadoop2.7  to /Users/yennanliu/spark
4) install python spark API library : pyspark
5) declare env parameter
6) run the spark via command : pysark 
Ref :
JAVA JDK can be downloaded here 
http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
#-------------------
COMMENT1

# get ops route 
my_route=$(pwd)
echo $my_route

echo '>>>>>>>>>>>> STEP 1)  Set up dev env'
#yes Y | conda create -n pyspark_dev python=3.5
#source activate pyspark_dev

echo '>>>>>>>>>>>> STEP 2)  Install pyspark'
# download here  : http://spark.apache.org/downloads.html
cd ~
wget --quiet http://apache.mirror.anlx.net/spark/spark-2.4.1/spark-2.4.1-bin-hadoop2.7.tgz
echo 'location :'
pwd 
echo 'file :'
ls 
tar -xzf $my_route/spark-2.4.1-bin-hadoop2.7.tgz
cd ~
cp -R $my_route/spark-2.4.1-bin-hadoop2.7 $my_route/spark
# install python pyspark library 
pip install --upgrade pip && pip install pyspark && pip freeze list 

echo '>>>>>>>>>>>> STEP 3)  Declare env parameter'
# declare env parameter
export SPARK_HOME=$my_route/spark
export PATH=$SPARK_HOME/bin:$PATH

echo '######################## SPARK INSTALL SUCCESS ########################'
echo 'PLEASE RUN it via cona env : pyspark_dev '
echo 'source activate pyspark_dev && export SPARK_HOME=/Users/$USER/spark && export PATH=$SPARK_HOME/bin:$PATH && pyspark'
echo '######################## SPARK INSTALL SUCCESS ########################'
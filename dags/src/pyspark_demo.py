# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row
from operator import add
# ------------------------------------------------------
# spark config 
conf = SparkConf().setAppName("spark dev")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
sc
# create RDD
intRDD = sc.parallelize([6,7,1,2,0])
intRDD2 = sc.parallelize(["apple", "car", "pan"])
print (intRDD.collect())
print (intRDD2.collect())
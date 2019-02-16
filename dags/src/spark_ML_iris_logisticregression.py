import numpy as np
import pandas as pd
import pyspark
import os
import sys

from pyspark.sql.functions import *
from pyspark.ml.classification import *
from pyspark.ml.evaluation import *
from pyspark.ml.feature import *



# start Spark session
spark = pyspark.sql.SparkSession.builder.appName('Iris').getOrCreate()

# print runtime versions
print ('****************')
print ('Python version: {}'.format(sys.version))
print ('Spark version: {}'.format(spark.version))
print ('****************')

def main():
	# load iris.csv into Spark dataframe
	### load iris from sklearn dataset
	from sklearn import datasets
	data =  datasets.load_iris()
	df= pd.DataFrame(data.data)
	df.columns = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']
	df['class'] = data['target']
	df.to_csv('iris.csv',index=False)
	###

	data = spark.createDataFrame(pd.read_csv('iris.csv'))
	data = data.withColumn("sepal-length", data["sepal-length"].cast("float"))
	data = data.withColumn("sepal-width", data["sepal-width"].cast("float"))
	data = data.withColumn("petal-length", data["petal-length"].cast("float"))
	data = data.withColumn("petal-width", data["petal-width"].cast("float"))
	data = data.withColumn("class", data["class"].cast("float"))
	print("First 10 rows of Iris dataset:")
	data.show(10)

	# vectorize all numerical columns into a single feature column
	feature_cols = data.columns[:-1]
	assembler = pyspark.ml.feature.VectorAssembler(inputCols=feature_cols, outputCol='features')
	data = assembler.transform(data)

	# convert text labels into indices
	data = data.select(['features', 'class'])
	label_indexer = pyspark.ml.feature.StringIndexer(inputCol='class', outputCol='label').fit(data)
	data = label_indexer.transform(data)

	# only select the features and label column
	data = data.select(['features', 'label'])
	print("Reading for machine learning")
	data.show(10)

	# change regularization rate and you will likely get a different accuracy.
	reg = 0.01
	# load regularization rate from argument if present
	if len(sys.argv) > 1:
	    reg = float(sys.argv[1])


	# use Logistic Regression to train on the training set
	train, test = data.randomSplit([0.70, 0.30])
	lr = pyspark.ml.classification.LogisticRegression(regParam=reg)
	model = lr.fit(train)

	# predict on the test set
	prediction = model.transform(test)
	print("Prediction")
	prediction.show(10)

	# evaluate the accuracy of the model using the test set
	evaluator = pyspark.ml.evaluation.MulticlassClassificationEvaluator(metricName='accuracy')
	accuracy = evaluator.evaluate(prediction)

	print()
	print('#####################################')
	print('Regularization rate is {}'.format(reg))
	print("Accuracy is {}".format(accuracy))
	print('#####################################')
	print()

if __name__ == '__main__':
	main()

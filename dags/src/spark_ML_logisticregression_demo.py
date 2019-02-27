# LogisticRegression spark demo 

from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import (BinaryClassificationEvaluator,MulticlassClassificationEvaluator)
from pyspark.ml import Pipeline
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator

def main():
	spark = SparkSession.builder.appName('logstic_regression').getOrCreate()
	my_data = spark.read.format('libsvm').load('data/sample_libsvm_data.txt')
	my_data.show()
	print (' STEP 1) ----------  SIMPLE TRAIN ')
	lr_train, lr_test =  my_data.randomSplit([0.7, 0.3])
	# train on train set 
	final_model = LogisticRegression()
	fit_final = final_model.fit(lr_train)
	# prediction on test set 
	prediction_and_labels = fit_final.evaluate(lr_test)
	prediction_and_labels.predictions.show()
	# evaluate 
	my_eval = BinaryClassificationEvaluator()
	my_final_roc = my_eval.evaluate(prediction_and_labels.predictions)
	my_final_roc
	print (' STEP 2) ----------  GRID SEARCH TRAIN ')
	lr = LogisticRegression()
	pipeline = Pipeline(stages=[lr])
	paramGrid = ParamGridBuilder() \
			.addGrid(lr.regParam, [0.0, 10.0 , 30.0]) \
			.build()
	print ('-'*70) 
	print ('paramGrid : ', paramGrid)
	print ('-'*70) 
	crossval = CrossValidator(estimator=pipeline,
	                      estimatorParamMaps=paramGrid,
	                      evaluator=RegressionEvaluator(metricName="rmse"),
	                      numFolds=2)  # use 3+ folds in practice
	cvModel = crossval.fit(lr_train)
	prediction = cvModel.transform(lr_test)
	prediction.show()
	# evaluate with best model : to fix 
	#prediction_and_labels = cvModel.bestModel.evaluate(lr_test)
	#prediction_and_labels.predictions.show()



if __name__ == '__main__':
	main()
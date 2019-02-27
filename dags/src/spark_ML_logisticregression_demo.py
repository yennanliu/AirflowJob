# LogisticRegression spark demo 

from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression

def main():
	spark = SparkSession.builder.appName('logstic_regression').getOrCreate()
	my_data = spark.read.format('libsvm').load('data/sample_libsvm_data.txt')
	my_data.show()
	lr_train, lr_test =  my_data.randomSplit([0.7, 0.3])
	# train on train set 
	final_model = LogisticRegression()
	fit_final = final_model.fit(lr_train)
	# prediction on test set 
	prediction_and_labels = fit_final.evaluate(lr_test)
	prediction_and_labels.predictions.show()
	# evaluate 

	from pyspark.ml.evaluation import (BinaryClassificationEvaluator,
	                                    MulticlassClassificationEvaluator)
	my_eval = BinaryClassificationEvaluator()
	my_final_roc = my_eval.evaluate(prediction_and_labels.predictions)
	my_final_roc

if __name__ == '__main__':
	main()
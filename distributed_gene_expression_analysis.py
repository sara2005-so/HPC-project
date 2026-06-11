from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

print("======================================")
print("Distributed Gene Expression Analysis")
print("======================================")

# Create Spark session
spark = SparkSession.builder \
    .appName("GeneExpressionAnalysis") \
    .getOrCreate()

# Load gene expression dataset
df = spark.read.csv(
    "bioinfo_data/leukemia_expression.csv",
    header=True,
    inferSchema=True
)

print("\nDataset Preview:")
df.show()

print("\nDataset Statistics:")
df.describe().show()

# Feature engineering
assembler = VectorAssembler(
    inputCols=["gene1", "gene2", "gene3"],
    outputCol="features"
)

data = assembler.transform(df)

# Split dataset into training and testing sets
train_data, test_data = data.randomSplit(
    [0.8, 0.2],
    seed=42
)

# Train Logistic Regression model
lr = LogisticRegression(
    featuresCol="features",
    labelCol="label"
)

model = lr.fit(train_data)

# Generate predictions
predictions = model.transform(test_data)

# Evaluate model performance
evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = evaluator.evaluate(predictions)

print("\n======================================")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("[SUCCESS] Distributed Gene Expression Analysis Complete!")
print("======================================")

spark.stop()
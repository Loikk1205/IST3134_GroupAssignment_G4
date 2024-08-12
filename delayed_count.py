from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("SparkTextFileValueCount") \
    .getOrCreate()

# Access SparkContext from SparkSession
sc = spark.sparkContext

# Read text file from HDFS
rdd = sc.textFile("hdfs:///Group_Asg/DelayedAirlines.txt")

# Map each line to (value, 1)
pairs = rdd.map(lambda line: (line, 1))

# Reduce by key to count occurrences
counts = pairs.reduceByKey(lambda a, b: a + b)

# Save the results to an output file in HDFS
counts.saveAsTextFile("hdfs:///Group_Asg/Delayed_Airline_Count.txt")

# Stop SparkSession
spark.stop()
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("CombineOutputFiles") \
    .getOrCreate()

# Access SparkContext from SparkSession
sc = spark.sparkContext

# Read the part files from HDFS
rdd = sc.textFile("hdfs:///Group_Asg/Delayed_Airline_Count.txt/part-*")

# Save the combined result to a single text file in HDFS
rdd.coalesce(1).saveAsTextFile("hdfs:///Group_Asg/Delayed_Combined_Output.txt")

# Stop SparkSession
spark.stop()












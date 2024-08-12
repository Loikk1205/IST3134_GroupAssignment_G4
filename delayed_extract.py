from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("ExtractCancelledAirlines") \
    .getOrCreate()

# Load the CSV file from HDFS
df = spark.read.option("header", "true").csv("hdfs:///Group_Asg/Combined_Flights_2022.csv")

# Filter rows where the 'Cancelled' column is 'true'
delayed_flights_df = df.filter(df["DepDelay"].cast("float") > 1)

# Extract the 'Airline' column from the filtered DataFrame
airline_column_df = delayed_flights_df.select("Airline")

# Save the 'Airline' column data to a text file in HDFS
airline_column_df.rdd.flatMap(lambda x: x).saveAsTextFile("hdfs:///Group_Asg/DelayedAirlines.txt")

# Stop the SparkSession
spark.stop()

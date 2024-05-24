from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, sum
import time

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SparkUIExample") \
    .config("spark.executor.instances", "3") \
    .config("spark.executor.memory", "2g") \
    .config("spark.executor.cores", "2") \
    .getOrCreate()

# Read the CSV data
df = spark.read.csv("/tmp/sample_data", header=True, inferSchema=True)

# Stage 1: Filter rows where value > 50
filtered_df = df.filter(col("value") > 50)

# Stage 2: Group by 'name' and calculate aggregate metrics
aggregated_df = filtered_df.groupBy("name").agg(
    count("*").alias("count"),
    avg("value").alias("avg_value"),
    sum("value").alias("sum_value")
)

# Stage 3: Sort by 'sum_value' in descending order
sorted_df = aggregated_df.orderBy(col("sum_value").desc())

# Stage 4: Show the top 10 results
top_10 = sorted_df.limit(10)
top_10.show()

# Write the result to disk (Parquet format)
top_10.write.mode("overwrite").parquet("output/top_10")

top_10.show()

time.sleep(180)

# Stop Spark session
spark.stop()


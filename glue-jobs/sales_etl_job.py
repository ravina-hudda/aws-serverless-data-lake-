import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import year, month, to_date, col

# Get job name
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Create Spark and Glue contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Initialize Glue job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read raw CSV data
df = spark.read.option("header", "true").csv(
    "s3://ravina-aws-data-lake-hyd/raw/sales/"
)

# Fix schema and add partitions
df = df.withColumn("amount", col("amount").cast("double")) \
       .withColumn("order_date", to_date("order_date")) \
       .withColumn("year", year("order_date")) \
       .withColumn("month", month("order_date"))

# Write Parquet output
df.write.mode("overwrite") \
    .partitionBy("year", "month") \
    .parquet("s3://ravina-aws-data-lake-hyd/processed/sales/")

job.commit()

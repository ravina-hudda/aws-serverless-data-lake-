# AWS Serverless Data Lake Pipeline

This project demonstrates an end-to-end **serverless Big Data pipeline on AWS**
using **Amazon S3, AWS Glue (Spark), and Amazon Athena**.

## Architecture
Data Source → S3 (Raw Zone) → Glue Crawler → Glue Spark ETL →  
S3 (Parquet + Partitioned) → Athena

## Technologies Used
- Amazon S3 (Data Lake)
- AWS Glue (Spark ETL, Crawlers, Data Catalog)
- Amazon Athena (Serverless Analytics)
- Apache Spark (PySpark)
- Parquet, CSV

## Data Flow
1. Raw CSV data is ingested into S3.
2. Glue Crawlers infer schema and create metadata.
3. Glue Spark job transforms CSV into partitioned Parquet format.
4. Optimized data is queried using Athena.

## Key Features
- Serverless architecture (no cluster management)
- Parquet conversion for performance optimization
- Partitioning to reduce query cost
- Schema handling and IAM-based access control

## Sample Athena Query
```sql
SELECT country, SUM(amount) AS total_sales
FROM sales
GROUP BY country;

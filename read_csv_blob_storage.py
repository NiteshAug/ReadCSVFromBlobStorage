# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Read CSV from Azure Blob Storage") \
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-azure:3.3.1") \
    .getOrCreate()

# Set your Azure Blob Storage credentials
azure_blob_storage_account_name = "<Azure Storage Account Name>"
azure_blob_storage_account_access_key = "<Azure Access Key>"
azure_blob_container = "<Azure Container Name>"
csv_file_path = "<Blob Csv File name>"

# Define the Azure Blob Storage URL
azure_blob_storage_url = f"wasbs://{azure_blob_container}@{azure_blob_storage_account_name}.blob.core.windows.net/{csv_file_path}"

# Read the CSV file into a DataFrame
df = spark.read.csv(azure_blob_storage_url, header=True, inferSchema=True)

# Group by class and year, and calculate the total number of students
total_students_per_class_year = df.groupBy("className", "years") \
    .agg(F.sum("num_of_students").alias("total_students"))

# Show the DataFrame
total_students_per_class_year.show()

# Stop the SparkSession
spark.stop()

# ReadCSVPySparkIntoDataframe
read the CSV file in pyspark into Dataframe from azure blob storage

# Add Azure access key
azure_blob_storage_account_access_key = "<Azure Access Key>"

# Install PySpark
pip install pyspark

# Install azure blob storage
pip install azure-storage-blob

# Add Some dependency which are missing in .m2 folder
1. Download from maven repository or official website
2. download httpcore-4.4.13.jar and add to C:\Users\Admin\.m2\repository\org\apache\httpcomponents\httpcore\4.4.13
3. download httpclient-4.5.13.jar and add to C:\Users\Admin\.m2\repository\org\apache\httpcomponents\httpclient\4.5.13
4. download azure-storage-8.6.5.jar and add to C:\hadoop\bin (create folder in C drive)
5. download hadoop-azure-3.3.1.jar and add to C:\hadoop\bin
6. Set HADOOP_HOME environment in environment variable

# Add config in spark session
.config("spark.jars.packages", "org.apache.hadoop:hadoop-azure:3.3.1") \

# ignore below exception
![img.png](img%2Fimg.png)

# findout Total number ofstudents per class, per year
![img_1.png](img%2Fimg_1.png)

# in databricks workspace added this code in notebook and output is
![img_2.png](img%2Fimg_2.png)
=======
# ReadCSVPySparkIntoDataframe
read the CSV file in pyspark into Dataframe from azure blob storage

# Add Azure access key
azure_blob_storage_account_access_key = "<Azure Access Key>"

# Install PySpark
pip install pyspark

# Install azure blob storage
pip install azure-storage-blob

# Add Some dependency which are missing in .m2 folder
1. Download from maven repository or official website
2. download httpcore-4.4.13.jar and add to C:\Users\Admin\.m2\repository\org\apache\httpcomponents\httpcore\4.4.13
3. download httpclient-4.5.13.jar and add to C:\Users\Admin\.m2\repository\org\apache\httpcomponents\httpclient\4.5.13
4. download azure-storage-8.6.5.jar and add to C:\hadoop\bin (create folder in C drive)
5. download hadoop-azure-3.3.1.jar and add to C:\hadoop\bin
6. Set HADOOP_HOME environment in environment variable

# Add config in spark session
.config("spark.jars.packages", "org.apache.hadoop:hadoop-azure:3.3.1") \

# ignore below exception
![img.png](img%2Fimg.png)

# findout Total number ofstudents per class, per year
![img_1.png](img%2Fimg_1.png)

# in databricks workspace added this code in notebook and output is
![img_2.png](img%2Fimg_2.png)
![img_3.png](img%2Fimg_3.png)

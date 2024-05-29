from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

# Connection string for Azure Storage account
connection_string = "<Azure-Connection-String>"

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Name of the container where your file is stored
container_name = "<Azure-Container-Name>"

# Name of the file you want to read
blob_name = "<Blob CSV File>"

# Get a BlobClient to interact with the specific blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download the blob's content as a stream
downloaded_blob = blob_client.download_blob()

# Read the content of the blob into a DataFrame
content = downloaded_blob.content_as_text()
df = pd.read_csv(io.StringIO(content), header=None, names=["pyId", "className", "section", "years", "num_of_students"])

# Now you have your DataFrame ready to use
print(df.head())

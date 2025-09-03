import chromadb
import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client("s3")
bucket = "datascrapebucket"
key = "combined_data.csv"

response = s3.get_object(Bucket=bucket, Key=key)
csv_body = response['Body'].read().decode('utf-8') # Read and decode the stream
data = pd.read_csv(StringIO(csv_body))

data = data.fillna("")
data["document"] = "Post Title: " + data["Title"] + " Post Content: " + data["Post_Text"] + "Top Response: " + data["Top_Comment"]

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection(name="my_collection")

collection.add(
    documents=data["Post_Text"].tolist(),
    ids=data["Post_URL"].tolist()
)

print("Successfully added ", collection.count(), " documents to the database.")
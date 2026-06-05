import requests
import pandas as pd
import boto3
from io import StringIO

# API Call
resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Convert DataFrame to CSV format
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)
print("Hi")
# AWS S3 Details
bucket_name = "batch-may-15-2026"
file_name = "landing_zone/posts_data.csv"

# Create S3 Client
s3_client = boto3.client("s3")

# Upload CSV to S3
s3_client.put_object(
    Bucket=bucket_name,
    Key=file_name,
    Body=csv_buffer.getvalue()
)

print(f"File uploaded successfully to s3://{bucket_name}/{file_name}")
import functions_framework
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
import time

# This function is triggered by changes in a Google Cloud Storage bucket
@functions_framework.cloud_event
def handle_gcs_event(cloud_event):
    data = cloud_event.data

    # Extracting event details
    event_id = cloud_event["id"]
    event_type = cloud_event["type"]
    bucket = data["bucket"]
    filename = data["name"]
    metageneration = data["metageneration"]
    time_created = data["timeCreated"]
    updated = data["updated"]

    # Logging the event details
    print(f"Event ID: {event_id}")
    print(f"Event Type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {filename}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {time_created}")
    print(f"Updated: {updated}")

    # Trigger the loading of data into BigQuery
    load_data_into_bq(filename)


# BigQuery parameters
DATASET_NAME = 'sales'
TABLE_NAME = 'orders'

def load_data_into_bq(filename):
    client = bigquery.Client()

    # Reference to the BigQuery table
    table_ref = client.dataset(DATASET_NAME).table(TABLE_NAME)

    # Configuration for loading the data
    job_config = LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.autodetect = True

    # URI of the file in Google Cloud Storage
    uri = f'gs://bkt-sales-data/{filename}'
    
    # Loading the data into BigQuery
    load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
    
    # Wait for the job to complete
    load_job.result()  
    time.sleep(10)  # Optional: you might want to adjust this based on your needs

    # Retrieve and log the number of rows loaded
    num_rows = load_job.output_rows
    print(f"{num_rows} rows loaded into {TABLE_NAME}.")

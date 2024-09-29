# Google Cloud Data Analytics Project

This repository contains code and configuration files for the **Google Cloud Data Analytics Project**. This project demonstrates the integration of several GCP services to create an efficient and automated data pipeline for sales data.

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)

## Overview

This project allows users to easily upload sales data files through a web portal built with Python Flask. The uploaded files are then processed through various GCP services to provide insights into sales metrics. Here’s a brief outline of the key components:

- **Web Portal**: Built with Python Flask to allow users to upload sales data files.
- **Storage**: Uploaded files are stored in a Google Cloud Storage (GCS) bucket.
- **Cloud Function**: Automatically triggered when a file is uploaded to the GCS bucket, extracts data from the file, and loads it into BigQuery.
- **ETL Process**: Extract, Transform, Load process implemented to handle data from raw upload to processed state.
- **Reporting**: Summary views and dashboards in Looker Studio for key metrics, with filtering and drill-down capabilities.

![Web Portal](link_to_web_portal_image)  <!-- Replace with actual image link -->
![Data Pipeline Architecture](link_to_architecture_image)  <!-- Replace with actual image link -->

## Architecture

![Architecture Diagram](link_to_architecture_diagram)  <!-- Replace with actual image link -->
This architecture diagram illustrates the flow of data from the web portal to storage, processing, and reporting.

## Getting Started

### Prerequisites
- Google Cloud Platform account
- Python 3.x
- Flask
- Google Cloud SDK
- Required libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/google-cloud-data-analytics-project.git
   cd google-cloud-data-analytics-project
2. Set up a virtual environment:
   python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

3.Install required packages:
pip install -r requirements.txt

4. Configure your Google Cloud project and set up authentication:

5. Set your Google Cloud environment variables:
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"

How to Use
Run the Flask application:

bash
python main.py
Navigate to http://localhost:5000 in your web browser.

Use the upload form to select and upload your sales data files.

Once uploaded, the Cloud Function will automatically trigger, and data will be loaded into BigQuery.

Access summary views and dashboards in Looker Studio for analysis.

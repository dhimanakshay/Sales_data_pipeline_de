from flask import Flask, request, render_template, redirect, url_for, flash
from google.cloud import storage
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'mysecretkey'  # Used for flash messages

# Specify the Google Cloud Storage bucket name
GCS_BUCKET_NAME = 'bkt-sales-data'

# Create a Google Cloud Storage client
storage_client = storage.Client()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the file part is present in the request
        if 'file' not in request.files:
            flash('No file part found in the request.')
            return redirect(request.url)

        file = request.files['file']

        # Validate that a file has been selected
        if file.filename == '':
            flash('Please select a file to upload.')
            return redirect(request.url)

        # Process the file upload to GCS
        if file:
            try:
                # Secure the filename before uploading
                filename = secure_filename(file.filename)
                bucket = storage_client.bucket(GCS_BUCKET_NAME)
                blob = bucket.blob(filename)
                blob.upload_from_file(file)
                flash(f'Successfully uploaded "{filename}" to {GCS_BUCKET_NAME}.')
                return redirect(url_for('upload_file'))
            except Exception as e:
                flash(f'Error occurred during file upload: {e}')
                return redirect(request.url)
    
    # Display the file upload page
    return render_template('index.html')

if __name__ == '__main__':
    # Set the path for the Google Cloud service account key
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/service-account-file.json'
    app.run(debug=True)

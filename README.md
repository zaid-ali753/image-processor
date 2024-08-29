# Image Processor

A FastAPI application for uploading and processing CSV files asynchronously. Includes endpoints for file upload, status checking, and webhook notifications.

## Features

- **Upload CSV Files:** Asynchronously process CSV files uploaded by users.
- **Check Status:** Retrieve the processing status of an uploaded file.
- **Webhook Notifications:** Receive processing status notifications via a webhook.

## Requirements

- Python 3.8 or higher
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite (or any other supported database)
- Requests

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/image-processor.git
   cd image-processor
2. Create a Virtual Environment
   ```bash

   python -m venv env
3. Activate the Virtual Environment
   ```On Windows:

   bash
   .\env\Scripts\activate
   On macOS/Linux:

   bash
   source env/bin/activate
4. Install Dependencies
   ```bash

   pip install -r requirements.txt
Configuration
Update app/db/database.py with your database configuration.

5.Running the Application

   ```Start the FastAPI application with Uvicorn:

   bash

   uvicorn app.main:app --reload
```

Access the API Documentation:
Open your browser and go to http://127.0.0.1:8000/docs for the interactive API documentation or http://127.0.0.1:8000/redoc for the alternative documentation.

API Endpoints
1. Upload CSV File
URL: image/upload/

Method: POST

Request:

Headers:

Content-Type: multipart/form-data
Body:

Form-data with a key file (Type: file, Description: The CSV file to upload)
Response:
 ```Success (200 OK):

   {
       "request_id": "string"
   }
   Error (400 Bad Request):
   
   {
       "detail": "Only CSV files are supported"
   }
```
2. Get Processing Status
URL: image/status/{request_id}

Method: GET

URL Params:

request_id (string): The ID of the request to check the status for.
Response:

   ```Success (200 OK):
   {
       "request_id": "string",
       "status": "string",
       "details": "string"
   }
   Error (404 Not Found):
   
   {
       "detail": "Request ID not found"
   }
```
Webhook Notifications
Endpoint: Configure a webhook URL to receive status updates.

Method: POST

   ```Payload:
   {
       "request_id": "string",
       "status": "string",
       "details": "string"
   }
   ```
Troubleshooting
ModuleNotFoundError: Ensure all dependencies are installed. Use pip install -r requirements.txt to install required packages.
FileNotFoundError: Ensure the temp directory exists or is correctly created. Verify directory permissions.

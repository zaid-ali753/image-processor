import requests
from app import crud
from sqlalchemy.orm import Session

async def process_csv(file_location: str, request_id: str, db: Session):

    crud.update_processing_status(db, request_id, "Completed")

    webhook_url = "http://your-webhook-url.com/notify"
    payload = {
        "request_id": request_id,
        "status": "Completed",
        "file_location": file_location
    }
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to send webhook notification: {e}")

from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from app.database import SessionLocal, engine
from app.models import Base
from app.crud import create_request, get_request_by_id, update_request_status, update_output_images
from app.image_processor import process_images_async
from app.schemas import RequestStatus
import uuid

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...), background_tasks: BackgroundTasks):
    content = await file.read()
    csv_data = content.decode().splitlines()

    if not csv_data:
        raise HTTPException(status_code=400, detail="Empty CSV file.")
    
    request_id = str(uuid.uuid4())
    
    background_tasks.add_task(process_images_async, csv_data, request_id)

    db = SessionLocal()
    try:
        create_request(db, request_id)
    finally:
        db.close()

    return {"request_id": request_id}

@app.get("/status/{request_id}", response_model=RequestStatus)
async def check_status(request_id: str):
    db = SessionLocal()
    try:
        request = get_request_by_id(db, request_id)
        if not request:
            raise HTTPException(status_code=404, detail="Request ID not found.")
        return request
    finally:
        db.close()

@app.post("/webhook")
async def webhook(request_id: str, output_image_urls: list[str]):
    db = SessionLocal()
    try:
        update_output_images(db, request_id, output_image_urls)
        update_request_status(db, request_id, "Completed")
    finally:
        db.close()

    return {"status": "success"}

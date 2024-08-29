from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException, Depends
from sqlalchemy.orm import Session
import uuid
from app import crud, tasks
from app.db.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload/")
async def upload_csv(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)
):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")

    file_location = f"temp/{uuid.uuid4()}.csv"
    with open(file_location, "wb") as file_object:  
        file_object.write(await file.read())  

    request_id = str(uuid.uuid4())
    background_tasks.add_task(tasks.process_csv, file_location, request_id, db)
    
    return {"request_id": request_id}

@router.get("/status/{request_id}")
def get_status(request_id: str, db: Session = Depends(get_db)):
    status = crud.get_processing_status(db, request_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Request ID not found")
    
    return status

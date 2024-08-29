from sqlalchemy.orm import Session
from app.models import ProcessingRequest

def get_processing_status(db: Session, request_id: str):
    return db.query(ProcessingRequest).filter(ProcessingRequest.id == request_id).first()

def create_processing_request(db: Session, request: ProcessingRequest):
    db.add(request)
    db.commit()
    db.refresh(request)
    return request

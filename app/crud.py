from sqlalchemy.orm import Session
from app.models import Request

def create_request(db: Session, request_id: str):
    db_request = Request(request_id=request_id)
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

def get_request_by_id(db: Session, request_id: str):
    return db.query(Request).filter(Request.request_id == request_id).first()

def update_request_status(db: Session, request_id: str, status: str):
    request = get_request_by_id(db, request_id)
    if request:
        request.status = status
        db.commit()
        db.refresh(request)
    return request

def update_output_images(db: Session, request_id: str, output_image_urls: list[str]):
    request = get_request_by_id(db, request_id)
    if request:
        request.output_image_urls = ",".join(output_image_urls)
        db.commit()
        db.refresh(request)
    return request

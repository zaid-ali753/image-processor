from sqlalchemy import Column, String, Integer, Text
from app.db.database import Base

class ProcessingRequest(Base):
    __tablename__ = "processing_requests"

    id = Column(String, primary_key=True, index=True)
    status = Column(String, index=True)
    processed_images = Column(Integer, default=0)
    total_images = Column(Integer, default=0)
    product_name = Column(String)
    input_image_urls = Column(Text)
    output_image_urls = Column(Text)

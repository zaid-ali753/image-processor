from sqlalchemy import Column, String, Integer, Text
from app.database import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(String, unique=True, index=True)
    status = Column(String, default="Processing")
    input_image_urls = Column(Text, default="")
    output_image_urls = Column(Text, default="")

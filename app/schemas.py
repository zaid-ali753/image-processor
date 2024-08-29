from pydantic import BaseModel
from typing import Optional, List

class RequestStatus(BaseModel):
    request_id: str
    status: str
    input_image_urls: Optional[str]
    output_image_urls: Optional[str]

    class Config:
        orm_mode = True

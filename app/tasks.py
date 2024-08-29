import os
import asyncio
from sqlalchemy.orm import Session
from app.models import ProcessingRequest
from app.crud import create_processing_request
from app.image_processor import process_images

async def process_csv(file_location: str, request_id: str, db: Session):
    with open(file_location, 'r') as file:
        product_name = "Example Product"
        image_urls = [
            "https://example.com/image1.jpg",
            "https://example.com/image2.jpg",
            "https://example.com/image3.jpg"
        ]
        
    compressed_images = await process_images(image_urls)
    
    output_image_urls = [
        "https://example.com/processed_image1.jpg",
        "https://example.com/processed_image2.jpg",
        "https://example.com/processed_image3.jpg"
    ]
    
    request = ProcessingRequest(
        id=request_id,
        status="completed",
        processed_images=len(output_image_urls),
        total_images=len(image_urls),
        product_name=product_name,
        input_image_urls=",".join(image_urls),
        output_image_urls=",".join(output_image_urls)
    )
    create_processing_request(db, request)

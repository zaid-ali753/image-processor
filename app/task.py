import asyncio
from app.image_processor import download_image, compress_image
from app.database import SessionLocal
from app.crud import update_request_status, update_output_images

async def process_images_async(csv_data: list[str], request_id: str):
    input_urls = []
    output_urls = []
    
    for row in csv_data[1:]:  # Skipping header
        columns = row.split(",")
        input_urls.append(columns[2:])  # Collecting image URLs

    # Process each image
    for image_urls in input_urls:
        compressed_urls = []
        for url in image_urls:
            img = await download_image(url)
            if img:
                compressed_img = await compress_image(img)
                # Upload compressed_img to cloud storage and get output URL
                compressed_url = upload_to_cloud(compressed_img)  # Placeholder
                compressed_urls.append(compressed_url)
        
        output_urls.append(compressed_urls)
    
    # Update DB
    db = SessionLocal()
    try:
        update_request_status(db, request_id, "Processing completed")
        update_output_images(db, request_id, output_urls)
    finally:
        db.close()

    # Call webhook
    await send_webhook(request_id, output_urls)

async def send_webhook(request_id: str, output_image_urls: list[str]):
    async with aiohttp.ClientSession() as session:
        webhook_url = "http://webhook-service-url.com/webhook"
        payload = {
            "request_id": request_id,
            "output_image_urls": output_image_urls
        }
        await session.post(webhook_url, json=payload)

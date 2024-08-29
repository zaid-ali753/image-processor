import aiohttp
import asyncio
from io import BytesIO
from PIL import Image

async def download_image(url: str) -> Image.Image:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                img_data = await response.read()
                image = Image.open(BytesIO(img_data))
                return image
            else:
                raise Exception(f"Failed to download image from {url}")

def compress_image(image: Image.Image, quality: int = 50) -> BytesIO:
    img_io = BytesIO()
    image.save(img_io, 'JPEG', quality=quality)
    img_io.seek(0)
    return img_io

async def process_image(url: str) -> BytesIO:
    image = await download_image(url)
    compressed_image = compress_image(image)
    return compressed_image

async def process_images(image_urls: list[str]) -> list[BytesIO]:
    tasks = [process_image(url) for url in image_urls]
    compressed_images = await asyncio.gather(*tasks)
    return compressed_images

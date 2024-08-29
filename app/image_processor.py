import aiohttp
from PIL import Image
from io import BytesIO

async def download_image(url: str) -> Image.Image:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                img_bytes = await response.read()
                img = Image.open(BytesIO(img_bytes))
                return img
            return None

async def compress_image(image: Image.Image) -> BytesIO:
    output = BytesIO()
    image.save(output, format='JPEG', quality=50)  # Compress to 50% quality
    output.seek(0)
    return output

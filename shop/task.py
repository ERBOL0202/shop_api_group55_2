from celery import shared_task
from PIL import Image
import io

@shared_task
def resize_image(image_bytes, width, height):
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((width, height))
    output = io.BytesIO()
    image.save(output, format='JPEG')
    return output.getvalue()
from io import BytesIO

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.files.base import ContentFile

from v1.models import Product

from PIL import Image

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


@receiver(pre_save, sender=Product)
def resize_image(sender, instance, **kwargs):
    if bool(instance.image):
        image = Image.open(instance.image)

        image_extention = instance.image.name.split(".")[-1]
        image_format = image_types.get(image_extention)

        length = settings.IMAGE_SIZE_DIMENSION

        if image.size[0] < image.size[1]:
            resized_image = image.resize((
                length,
                int(image.size[1] * (length / image.size[0]))
            ))
            required_loss = (resized_image.size[1] - length)
            resized_image = resized_image.crop(
                box=(0, required_loss / 2, length, resized_image.size[1] - required_loss / 2)
            )
        else:
            resized_image = image.resize((
                int(image.size[0] * (length / image.size[1])),
                length
            ))
            required_loss = resized_image.size[0] - length
            resized_image = resized_image.crop(
                box=(required_loss / 2, 0, resized_image.size[0] - required_loss / 2, length)
            )

        output_io = BytesIO()
        resized_image.save(output_io, format=image_format)
        output_io.seek(0)
        instance.image.save(instance.image.name, ContentFile(output_io.getvalue()), save=False)

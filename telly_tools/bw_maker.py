from PIL import Image
import io
from random import randint
import os


def bw_effect(user_image):
    """
    Save the colored image from user then convert its color to gray scheme.

    :param user_image: Colored image
    :return: B&W image
    """

    global image_path, bw_path, bw_image
    image = Image.open(io.BytesIO(user_image))
    image_path = "temp/user_image.jpg"
    image.save(image_path)
    image = image.convert('L')
    num = randint(1000000, 9999999)
    bw_path = f"temp/yourPDF{num}.png"
    image.save(bw_path)

    bw_image = open(bw_path, 'rb')

    return bw_image


def empty_temp():
    """
    clean the user image and output file after sending to user.

    :return: None
    """

    bw_image.close()
    os.remove(bw_path)
    os.remove(image_path)

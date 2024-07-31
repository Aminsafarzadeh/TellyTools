import pyqrcode
import os
from random import randint


def qrcode(link):
    """
    Get link from bot and make Qr png with unique name.

    :param link: text that user sent
    :return: qr code in png format
    """

    global image_path
    url = pyqrcode.create(link)
    num = randint(1000000, 9999999)
    image_path = f"temp/yourQRcode{num}.png"
    url.png(image_path, scale=20)
    qr_image = open(image_path, 'rb')
    return qr_image


def empty_temp():
    """
    clean the qr image after sending to user.

    :return: None
    """

    os.remove(image_path)

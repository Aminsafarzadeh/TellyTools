import pyqrcode
import os
from random import randint


def qrcode(link):
    """
    Get link from bot and make Qr png with unique name.

    :param link: text that user sent
    :return: qr code in png format
    """

    global num
    url = pyqrcode.create(link)
    num = randint(1000000, 9999999)
    url.png(f"temp/yourQRcode{num}.png", scale=20)
    qr_image = open(f'temp/yourQRcode{num}.png', 'rb')
    return qr_image


def empty_temp():
    """
    clean the qr image after sending to user.

    :return: None
    """

    os.remove(f'temp/yourQRcode{num}.png')

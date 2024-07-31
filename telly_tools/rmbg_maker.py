from rembg import remove
from PIL import Image
import io
from random import randint


def remover(input):
    """
    Get photo and remove background.

    :param input: user photo
    :return: photo without background
    """
    img = Image.open(io.BytesIO(input))
    output = remove(img)

    bio = io.BytesIO()
    num = randint(1000000, 9999999)
    bio.name = f'yourPhoto{num}.png'
    output.save(bio, 'PNG')
    bio.seek(0)
    return bio

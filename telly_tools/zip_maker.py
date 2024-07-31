import os
from zipfile import ZipFile
from random import randint


def zipfile(name, file):
    """
    Gets the user file and make zip file with unique name.
    """

    with open(name, 'wb') as f:
        f.write(file)

    global file_path, zipf
    num = randint(1000000, 9999999)
    file_path = f"temp/yourZip{num}.zip"
    with ZipFile(file_path, 'w') as zipfile:
        zipfile.write(name)

    zipf = open(file_path, 'rb')
    return zipf


def empty_temp():
    """
    clean the zip file after sending to user.

    :return: None
    """
    zipf.close()
    os.remove(file_path)

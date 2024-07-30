import os
from zipfile import ZipFile
from random import randint


def zipfile(name, file):
    with open(name, 'wb') as f:
        f.write(file)

    global num, zipf
    num = randint(1000000, 9999999)
    with ZipFile(f"temp/yourZip{num}.zip", 'w') as zipfile:
        zipfile.write(name)


    zipf = open(f"temp/yourZip{num}.zip", 'rb')
    return zipf



def empty_temp():
    """
    clean the zip file after sending to user.

    :return: None
    """
    zipf.close()
    os.remove(f"temp/yourZip{num}.zip")
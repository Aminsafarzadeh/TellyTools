from PIL import Image
from fpdf import FPDF
import io
from random import randint
import os


def img_to_pdf(user_image):
    """
    Get user image, save it and convert to PDF.

    :param user_image:
    :return: pdf output
    """

    global output, pdf_path, image_path
    image = Image.open(io.BytesIO(user_image))
    image_path = "temp/user_image.jpg"
    image.save(image_path)

    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path, x=10, y=10, w=pdf.w - 20)
    num = randint(1000000, 9999999)
    pdf_path = f"temp/yourPDF{num}.pdf"
    pdf.output(pdf_path)

    output = open(pdf_path, 'rb')
    return output


def empty_temp():
    """
    clean the user image and PDF file after sending to user.

    :return: None
    """

    output.close()
    os.remove(pdf_path)
    os.remove(image_path)

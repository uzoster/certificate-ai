from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4


def generate_pdf(image_path: str, uuid: str):

    pdf_path = f"app/static/certificates/{uuid}.pdf"

    c = canvas.Canvas(
        pdf_path,
        pagesize=landscape(A4)
    )

    width, height = landscape(A4)

    image = ImageReader(image_path)

    c.drawImage(
        image,
        0,
        0,
        width=width,
        height=height
    )

    c.save()

    return pdf_path
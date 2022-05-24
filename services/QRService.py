import os
import qrcode
from reportlab.platypus import SimpleDocTemplate
from reportlab import platypus
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Image
import pandas as pd
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display
PATH = "qr.png"


class HyperlinkedImage(Image, object):
    """Image with a hyperlink, adopted from http://stackoverflow.com/a/26294527/304209."""

    def __init__(
        self,
        filename,
        hyperlink=None,
        width=None,
        height=None,
        kind="direct",
        mask="auto",
        lazy=1,
        hAlign="CENTER",
    ):
        super(HyperlinkedImage, self).__init__(
            filename, width, height, kind, mask, lazy, hAlign=hAlign
        )
        self.hyperlink = hyperlink

    def drawOn(self, canvas, x, y, _sW=0):
        if self.hyperlink: 
            x1 = self._hAlignAdjust(x, _sW)
            y1 = y
            x2 = x1 + self._width
            y2 = y1 + self._height
            canvas.linkURL(
                url=self.hyperlink, rect=(x1, y1, x2, y2), thickness=0, relative=1
            )
        super(HyperlinkedImage, self).drawOn(canvas, x, y, _sW)


def create_qr(url: str, file_name: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    
    img = qr.make_image()
    with open(PATH, "wb") as qr:
        img.save(qr)
        build_pdf(pdf_path="books"+"\\"+str(file_name.strip())+".pdf", file_name=file_name, url=url)
    os.remove(PATH)

def build_pdf(pdf_path:str, file_name: str, url: str):
    pdfmetrics.registerFont(TTFont('Noto', 'fonts/Noto.ttf'))
    file_name = arabic_reshaper.reshape(file_name)
    file_name = get_display(file_name)
    items = []
    p_style = PS(name='Normal_CENTER', alignment=TA_CENTER,fontName='Noto',
    fontSize=30)
    items.append(HyperlinkedImage(PATH, url, 300, 300))
    items.append(platypus.Paragraph(file_name, p_style))
    doc = SimpleDocTemplate(pdf_path)
    doc.multiBuild(items)


def create_multiple_qr(data: list):
    df = pd.DataFrame(data)
    df[1].apply(check_hyperlink)
def check_hyperlink(t: tuple):
        if isinstance(t, tuple):  # IF the value has hyperlink
            create_qr(url=t[1],file_name= t[0])
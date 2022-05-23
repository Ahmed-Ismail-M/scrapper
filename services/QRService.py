import os
import qrcode
from reportlab.platypus import SimpleDocTemplate
from reportlab import platypus
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Image
import tempfile

PATH = "qr.png"
URL = f"https://ar.wikipedia.org/wiki/%D9%8A%D8%AD%D9%8A%D9%89_%D8%AD%D9%82%D9%8A"
pdf_PATH = "test.pdf"
# PATH = 'accounting1.png'

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


def create_qr(url: str):
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
        build_pdf(path=pdf_PATH)
    os.remove(PATH)

def build_pdf(path):
    # create_qr(URL)
    items = []
    text = """احمد""".encode('utf8')
    p_style = PS(name='Normal_CENTER', alignment=TA_CENTER,font='Arial',
    fontSize=30)
    items.append(HyperlinkedImage(PATH, URL, 300, 300))
    items.append(platypus.Paragraph(text,p_style))
    doc = SimpleDocTemplate(path)
    doc.multiBuild(items)
create_qr(URL)

# build_pdf("test2.pdf")

import qrcode
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.platypus import SimpleDocTemplate
from reportlab import platypus
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.pdfgen import canvas
from reportlab.platypus import Image


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
        """The only variable added to __init__() is hyperlink.

        It defaults to None for the if statement used later.
        """
        super(HyperlinkedImage, self).__init__(
            filename, width, height, kind, mask, lazy, hAlign=hAlign
        )
        self.hyperlink = hyperlink

    def drawOn(self, canvas, x, y, _sW=0):
        if self.hyperlink:  # If a hyperlink is given, create a canvas.linkURL()
            # This is basically adjusting the x coordinate according to the alignment
            # given to the flowable (RIGHT, LEFT, CENTER)
            x1 = self._hAlignAdjust(x, _sW)
            y1 = y
            x2 = x1 + self._width
            y2 = y1 + self._height
            canvas.linkURL(
                url=self.hyperlink, rect=(x1, y1, x2, y2), thickness=0, relative=1
            )
        super(HyperlinkedImage, self).drawOn(canvas, x, y, _sW)


def create_svg(url: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    img = qr.make_image()
    # img = qrcode.make(url, image_factory=qimg.SvgPathImage)
    # img = qrcode.mak
    with open(PATH, "wb") as qr:
        img.save(qr)


# def create_pdf(path, url):
#     create_svg(url)
#     img = svg2rlg(PATH)
#     renderPDF.drawToFile(img, path)


def create_from_string(path):
    create_svg(URL)
    items = []
    text = f"""
    <h1 style="color:red; font-size: xx-large;">
    Aly Ahmed Ismail</h1 >"""
    items.append(HyperlinkedImage(PATH, URL, 100, 100))
    items.append(platypus.Paragraph(text, PS("body")))
    doc = SimpleDocTemplate(path)
    
    doc.multiBuild(items)


# create_pdf('test.pdf', 'https://im-software.net/')
create_from_string("test2.pdf")

from reportlab.pdfgen import canvas
import qrcode
import qrcode.image.svg as qimg
import tempfile
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

PATH = 'qr.svg'
def create(url:str):
    img = qrcode.make(url,image_factory=qimg.SvgImage)
    with open(PATH,'wb') as qr:
        img.save(qr)

# def create_img():
#     img = qrcode.make('www.im-software.net',image_factory=qimg.SvgImage)
#     svg_file = tempfile.NamedTemporaryFile()
#     img.save(svg_file)
#     svg_file.flush()
#     img_rl = svg2rlg(svg_file.name)
#     svg_file.close()
#     return img_rl
def create_pdf(path):
    create('www.im-software.net')
    renderPDF.drawToFile(svg2rlg(PATH), PATH)

create_pdf('test.pdf')
import qrcode
import qrcode.image.svg as qimg
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.platypus import SimpleDocTemplate
from reportlab import platypus
from  reportlab.lib.styles import ParagraphStyle as PS
import os

PATH = 'qr.svg'
# PATH = 'accounting1.png'
def create_svg(url:str):
    img = qrcode.make(url,image_factory=qimg.SvgPathImage)
    with open(PATH,'wb') as qr:
        img.save(qr)

def create_pdf(path, url):
    create_svg(url)
    img = svg2rlg(PATH)
    renderPDF.drawToFile(img, path)
def create_from_string(path):
    create_svg('https://im-software.net/')
    items = []
    text = f"""<a href="/wiki/%D9%84%D8%B9%D8%A8%D8%A9_%D8%A7%D9%84%D9%86%D8%B3%D9%8A%D8%A7%D9%86">
    <img src="{PATH}" ></img></a>"""
    items.append(platypus.Paragraph(text, PS('body') ))
    doc = SimpleDocTemplate(path)
    doc.multiBuild(items)
# create_pdf('test.pdf', 'https://im-software.net/')
create_from_string('test2.pdf')
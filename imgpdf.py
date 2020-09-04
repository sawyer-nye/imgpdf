#!/usr/bin/env python3

import sys, os

from datetime import date
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from PIL import Image
from io import BytesIO

def handleWrongInput():
    print(f'For proper usage, type: {sys.argv[0]} file_1.png ... file_n.png output.pdf')
    sys.exit(0)

if (sys.argv[1] == '-h'):
    handleWrongInput()

imgs = []
pdf_name = sys.argv[-1]

if (pdf_name == "file.py"):
    pdf_name = f'{date.today().ctime()}.pdf'
if (".pdf" not in pdf_name):
    handleWrongInput() 


canvas = Canvas(pdf_name, pagesize=(8.5 * inch, 11 * inch))

# append each img path to imgs
for i in range(1, len(sys.argv)-1):
    print(f'Adding {sys.argv[i]} to {pdf_name}')

    img = Image.open(sys.argv[i])
    img_width, img_height = img.size

    if (img_width > (8 * inch)) or (img_height > (10 * inch)):
        img_width = 8 * inch

    rgb_img = img.convert("RGB")
    rgb_img.save(f'TEMP_{i}.jpg')

    canvas.drawImage(f'TEMP_{i}.jpg', (0.25 * inch), 0, 
                        width=img_width,
                        preserveAspectRatio=True,
                        anchor='s')

    canvas.showPage()
    
    os.remove(f'TEMP_{i}.jpg')


canvas.save()
#!/usr/bin/env python3

import sys, os, webbrowser

from datetime import date
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from PIL import Image

def printHelpMessage():
    print(f'For proper usage, type: {sys.argv[0]} file_1.png ... file_n.png output.pdf')
    sys.exit(0)

if (sys.argv[1] == '-h') or (sys.argv[1] == 'help'):
    printHelpMessage()

# output file name: last argument
pdf_name = sys.argv[-1]

if (pdf_name == 'file.py'):
    pdf_name = f'{date.today().ctime()}.pdf'
if ('.pdf' not in pdf_name):
    printHelpMessage() 

canvas = Canvas(pdf_name, pagesize=(8.5 * inch, 11 * inch))

# draw each image on a new page
for i in range(1, len(sys.argv)-1):
    print(f'Adding {sys.argv[i]} to {pdf_name}')

    img = Image.open(sys.argv[i])
    img_width, img_height = img.size

    if (img_width > (8 * inch)) or (img_height > (10 * inch)):
        img_width = 8 * inch

    rgb_img = img.convert('RGB')
    rgb_img.save(f'TEMP_{i}.jpg')

    canvas.drawImage(f'TEMP_{i}.jpg', (0.25 * inch), 0, 
                        width=img_width,
                        preserveAspectRatio=True,
                        anchor='s')

    canvas.showPage()
    
    os.remove(f'TEMP_{i}.jpg')

canvas.save()

print(f'Images successfully saved to {pdf_name}.')

if (input('Open in browser? [y/N] ').lower() == 'y'):
    webbrowser.open_new_tab('file://' + os.path.realpath(pdf_name))
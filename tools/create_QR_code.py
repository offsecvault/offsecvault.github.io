#!/bin/python3

import pyqrcode
import png

link = "URL"
qr_code = pyqrcode.create(link)
qr_code.png("image.png", scale=5)


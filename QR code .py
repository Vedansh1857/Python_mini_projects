import pyqrcode
import png
from pyqrcode import QRCode
QRstring = "https://www.stackoverflow.com/"
url =pyqrcode.create(QRstring)
url.png('D:\Some Python Projects\qrcode.png', scale=8)
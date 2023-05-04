import pyqrcode
from pyqrcode import QRCode
import png
website="https://en.wikipedia.org/wiki/Outline_of_space_science"
myQrcode=pyqrcode.create(website)
myQrcode.svg("Space.svg",scale=8)
myQrcode.png("Space.png",scale=6)
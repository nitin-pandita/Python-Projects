from dataclasses import dataclass
from matplotlib.pyplot import fill
import qrcode
import image

mycode = qrcode.QRCode(
    border=15,
    box_size=7,
    version=15
)

data = "https://www.youtube.com/channel/UCKZCA_3i1AoGJOJ0fBjbxtA"

mycode.add_data(data)
mycode.make(fit=True)
img = mycode.make_image(fill="red",back_color="white")

img.save("MyYoutube.png")
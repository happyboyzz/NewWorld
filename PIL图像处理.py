from PIL import Image,ImageDraw,ImageFont

im=Image.new("RGB", (3500,4000),"white")

text="5"
d=ImageDraw.Draw(im)
fot=ImageFont.truetype("C:\Windows\Fonts\STCAIYUN.TTF",2500)
d.text((1500,-200), text,fill="red",font=fot)
im.show()

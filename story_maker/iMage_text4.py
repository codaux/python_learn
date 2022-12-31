import arabic_reshaper 
from bidi.algorithm import get_display
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2

img =cv2.imread("image.jpg")
fontpath = "Dana-Regular.ttf" # <== download font
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
text="رضا شیخ سامانی تقدیم می‌کند 123456 امتحان می‌کنیم"
reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)


text_w, text_h = draw.textsize(text, font=font, direction="rtl")

draw = ImageDraw.Draw(img_pil)
draw.text((50, 80),bidi_text, font = font)
img = np.array(img_pil)
cv2.imshow("image with arabic", img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
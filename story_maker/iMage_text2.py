
import arabic_reshaper
from bidi.algorithm import get_display

from PIL import Image, ImageFont, ImageDraw 

W , H = (1080 , 1920)

file_name = 'image.jpg'
image = Image.open(file_name) 
font = ImageFont.truetype('Dana-Regular.ttf', 20 , encoding='utf-8')
draw = ImageDraw.Draw(image) 
#text = 'رضا شیخ سامانی تقدیم می‌کند 123456'
text = 'thderheherhe'
reshaped_text = arabic_reshaper.reshape(text) # correct its shape
bidi_text = get_display(reshaped_text) # correct its direction

w, h = draw.textsize(text)
print(w,h)

draw.text(((W-w)/2 , 400) , bidi_text , (0,94,94)) 
image.show()
from PIL import Image, ImageFont, ImageDraw 

my_image = Image.open("image.jpg")
title_font = ImageFont.truetype('Dana-Regular.ttf', 50)

title_text = "رضا شیخ سامانی W بسیار خوب D"

W , H = (1080 , 1920)

image_editable = ImageDraw.Draw(my_image)

#image_editable.text((540,200), title_text, (0, 94, 94), font=title_font)

w , h = image_editable.textsize(title_text)
image_editable.text(((W-w)/2 , 400), title_text, (0, 94, 94), font=title_font)

my_image.save("result.jpg")

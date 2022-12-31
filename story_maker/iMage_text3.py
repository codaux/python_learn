from PIL import Image, ImageDraw, ImageFont
import textwrap

# configuration
font_size = 36
width = 3840
height = 390
back_ground_color = (255, 255, 255)
font_size = 80
font_color = (50, 0, 0)
text = " وأيضا هذا النصح محبوب جدا جدا لذلك انا أفضلههذا النص مكتوب باللغةمكتوب باللغةمكتوب باللغةمكتوب باللغةمكتوب باللغة مكتوب باللغة العربية وهو واضح بشكل جميل"
wrapped = textwrap.fill(text, 100)
im = Image.new("RGB", (width, height), back_ground_color)
draw = ImageDraw.Draw(im)
unicode_font = ImageFont.truetype("Dana-Regular.ttf", 40)
# get text box size
# text_w, text_h = draw.textsize(wrapped, font=unicode_font, direction="rtl")
draw.text(
    (0, 0),  # top left corner
    # (width - text_w, 0), # top right corner
    # (width - text_w, height - text_h), # bottom right corner
    # (0, height - text_h),  # bottom left corner
    # ((width - text_w) // 2, (height - text_h) // 2),  # center
    # (width - text_w, (height - text_h) // 2),  # center vertical + start from right
    wrapped,
    font=unicode_font,
    fill=font_color,
    direction='rtl',
    language='ar',
    align='left',  # affect the second line of the text, set to right to see the last line aligned to the right
)
im.show()
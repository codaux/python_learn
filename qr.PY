from encodings import utf_8
import qrcode
import string
import random
import csv

my_codes_list = []
with open('my_codes.txt' , 'r') as x:
    my_codes_list = x.read().splitlines()
    x.close()

print(type(x))
print(my_codes_list)
data = []
for i in range(50):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if new_code not in my_codes_list:
        my_codes_list.append(new_code)
        #print(new_code)
        url = 'damtech.ir/p/' + new_code
        pic_path = 'D:\ddddddddddddddd\python_learn\\' + new_code + '.png'
        img = qrcode.make(url)
        #print(url)
        type(img)  # qrcode.image.pil.PilImage
        img.save(new_code + ".png")
        x = []
        x.append(new_code)
        x.append(url)
        x.append(pic_path)
        data.append(x)
all= ''
print(data)
for n in my_codes_list:
    all = all + n + '\n'
with open('my_codes.txt' , 'w') as x:
    x.write(all)

header = ["new_code", "url", "@pic_path2"]
with open('new_codes.csv', 'w', encoding='UTF_8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
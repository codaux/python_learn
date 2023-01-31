from os import error
import requests
from bs4 import BeautifulSoup
import shutil
import csv

data = []

def crawl (shenase):
    URL = "https://roboeq.ir/products/detail/" + str(shenase)
    page = requests.get(URL)
    print (page)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("h1")
    name = str(results).replace("<h1>","").replace("</h1>","")

    pic = str(soup.find(id="main_picture")).split("url('")[1].split("');")[0]
    image_url = "https://roboeq.ir" + pic
    print(image_url)
    filename = image_url.split("/")[-1]
    r = requests.get(image_url, stream = True ,  headers={"referer":URL})
    r.raw.decode_content = True
    with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
    folder = "D:\ddddddddddddddd\python_learn\\"
    pic_path = folder + filename

    return(shenase, name, pic_path)


def zoj (shenase1 , shenase2):
    a = crawl(shenase1)
    b = crawl(shenase2)
    c = a+b
    return(c)

kodha = []
while True:
    kod = input()
    if kod == "":
        break
    kodha.append(kod)

#print (kodha)
    
for kod in kodha:
    data.append(zoj(kod.split(" / ")[0] , kod.split(" / ")[1]))

print (data)

#print (str(crawl ("0101009")))
header = ["shenase1", "name1" , "@pic_path1" , "shenase2", "name2" , "@pic_path2"]
with open('data2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(data)

print ("yooooooooooooooooooooooooohooooooooooooooooooooooo")




import requests
from bs4 import BeautifulSoup
import shutil
import csv
data = []
def crawl (shenase):
    URL = "https://roboeq.ir/products/detail/" + str(shenase)
    page = requests.get(URL)
    #print (page)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("h1")
    name = str(results).replace("<h1>","").split(">")[1].split("</h1")[0]
    #print(name)
    price = str(soup.find("span" , class_="best-seller-last-price text-grey-600 line-through")).split()[4]
    new_price = str(soup.find("span" , class_="best-seller-price font-semibold")).split()[3]
    off = str(soup.find(class_="best-seller-percentage font-medium text-red-400")).split()[4].split("%")[0]
    ##print(off)
    pic = str(soup.find(class_="card-image main-pic main_picture")).split("url('")[1].split("');")[0]
    image_url = "https://roboeq.ir" + pic
    filename = image_url.split("/")[-1]
    print(image_url)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    r = requests.get(image_url, stream = True, headers=headers)
    print(r)
    r.raw.decode_content = True
    with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
    folder = "D:\ddddddddddddddd\python_learn\\"
    pic_path = folder + filename

    return(shenase, name , price , new_price , off , pic_path)

kodha = [
"1505019",
"1604046",
"1802202",
"2201004",
"1502014",
]
for kod in kodha:
    data.append(crawl(kod))
print (data)
#print (str(crawl ("0101009")))
header = ["shenase", "name" , "price" , "new_price" , "off" , "@pic_path"]
with open('data2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(data)
print ("yooooooooooooooooooooooooohooooooooooooooooooooooo")
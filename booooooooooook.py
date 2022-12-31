from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions() 
options.add_argument("C:/Users/reza/AppData/Local/Google/Chrome/User%20Data/Default/") #Path to your chrome profile
w = webdriver.Chrome(options=options)
w.get("https://reader.taaghche.com/lib/18335/%D8%AC%D8%B2%DB%8C%D8%B1%D9%87")

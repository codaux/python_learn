from selenium import webdriver
import pickle

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get('http://demo.guru99.com/test/cookie/selenium_aut.php')
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get('http://demo.guru99.com/test/cookie/selenium_cookie.php')
driver.application_cache
driver.get("https://reader.taaghche.com/lib/18338/%D8%AC%D9%85%D8%B9%D9%87%E2%80%8C%DB%8C%20%D8%AE%D8%A7%DA%A9%D8%B3%D8%AA%D8%B1%DB%8C")
from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://webscraper.io/test-sites/e-commerce/scroll')

shop_elems = driver.find_elements_by_xpath(
    "//div[@class='thumbnail']"
)


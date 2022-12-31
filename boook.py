from selenium import webdriver
driver = webdriver.Chrome()
driver.get_cookies
#driver.current_window_handle
driver.get("https://reader.taaghche.com/lib/18335/%D8%AC%D8%B2%DB%8C%D8%B1%D9%87")

#driver.get("https://fidibo.com/#loginModal")
driver.set_window_size(500, 800)


def screenshot_all_page(name_book):
    for this_p in range(int(driver.find_element_by_xpath('//*[@id="totalPages"]').text)):
        driver.save_screenshot(f'/PATH_FILE/{name_book}/{this_p}.png')
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div[1]/i').click()
screenshot_all_page('12_ghanon_zendegi')


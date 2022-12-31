from webbot import Browser
driver = Browser()

driver.go_to('https://fidibo.com/') 
driver.click('ورود و ثبت نام' , tag='span')
driver.click('ورود با ایمیل' , tag='span')
driver.type('rezasamani' , into='Username' , id='_username')

driver.type('pDNWTxp5k8xhP8E' , into='Password' , id='_password') # specific selection

driver.click('Login')
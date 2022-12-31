from webbot import Browser

URL = "https://farasoo.kimai.ir/en/login/"

web = Browser()
web.go_to('https://farasoo.kimai.ir/en/login/') 

web.type('rezasamani' , into='Username' , id='_username')
#web.click('NEXT' , tag='span')
web.type('pDNWTxp5k8xhP8E' , into='Password' , id='_password') # specific selection

web.click('Login')

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\\Users\\rishabhsingh\\Downloads\\chromedriver.exe"


lt_username = "rishabhsinghlambdatest"
lt_access_key = "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei"


desired_capabilities = {
	"browserName": "Chrome",
	"browserVersion": "113.0",
	"LT:Options": {
		"username": "rishabhsinghlambdatest",
		"accessKey": "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei",
		"visual": True,
		"video": True,
		"platformName": "Windows 10",
		"network": True,
		"project": "Untitled",
		"console": "info"
	}
}


lt_remote_url = "https://" + lt_username + ":" + lt_access_key + "@hub.lambdatest.com/wd/hub"


driver = webdriver.Remote(command_executor=lt_remote_url, desired_capabilities=desired_capabilities)


driver.get("https://www.hackerrank.com/")


html_code = "<h1>Hello world rishabh </h1>"
driver.execute_script("document.body.innerHTML='<h1>Hello world rishabh </h1>'")
time.sleep(10)


driver.quit()


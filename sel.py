from selenium import webdriver
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get('http://hypem.com/')
with open("./test.html", "w") as f:
    f.write(driver.page_source)

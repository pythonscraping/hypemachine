from selenium import webdriver
import time
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get('http://hypem.com')
driver.get('http://hypem.com/track/2mp1c/Cende+-+What+I+Want')


try :
    link = driver.find_elements_by_xpath("//div[@class='fav-pager']//a[contains(text(), 'Show more')]")
    link[0].click()
   
    for i in range(1,10):
        time.sleep(0.5)
        link = driver.find_elements_by_xpath("//div[@class='fav-pager']//a[contains(text(), 'Next')]")
        link[0].click()
except :
    print(" not found")


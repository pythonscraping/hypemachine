from selenium import webdriver
from threading import Thread
import time
import os

mainfolder = "./" + time.strftime("%d-%m-%Y")

if not os.path.exists(mainfolder):
    os.makedirs(mainfolder)


liste = ["latest","latest/remix","latest/noremix","popular","popular/remix","popular/noremix"]
for folder in liste:
    exactfolder = mainfolder + "/" + folder
    if not os.path.exists(exactfolder):
        os.makedirs(exactfolder)


driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get('http://hypem.com')

for folder in liste:
    exactfolder = mainfolder + "/" + folder
    for i in range(1,101):
        url = "http://hypem.com/" + folder + "/" + str(i) + "/"
        driver.get(url)
        filename = str(i)+".html"
        with open(mainfolder +"/" + folder + "/" + filename, "w") as f:
            f.write(driver.page_source)
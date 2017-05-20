from lxml import etree, html
import time 

import os

mainfolder = "./" + time.strftime("%d-%m-%Y")


parser = etree.HTMLParser()

listofsongs = []
for root, dirs, files in os.walk(mainfolder):
    for file in files:
        if file.endswith(".html"):
            try: 
                filetoparse = os.path.join(root, file)
                tree = etree.parse(filetoparse, parser)
                r = tree.xpath("//h3[@class='track_name']//a[@class='artist']/@href")
                for elem in r :
                    print(elem)
                    listofsongs.append(elem)
            except :
                pass


liste = ["artists"]
for folder in liste:
    exactfolder = mainfolder + "/" + folder
    if not os.path.exists(exactfolder):
        os.makedirs(exactfolder)


from selenium import webdriver
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get('http://hypem.com')


myset = set(listofsongs)
listofsongs2 = list(myset)

print(len(listofsongs2))
for elem in listofsongs2:
    filename = elem.split('/artist/')[1]+".html"
    print(filename)
    driver.get('http://hypem.com'+elem)
    with open(mainfolder +"/" + "artists" + "/" + filename, "w") as f:
            f.write(driver.page_source)
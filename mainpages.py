import requests
from threading import Thread



class Downloader(Thread):

    def __init__(self, pagenumber):
        Thread.__init__(self)
        self.pagenumber = pagenumber

    def run(self):
        url = "http://hypem.com/latest/" + str(self.pagenumber) + "/"
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.110 Chrome/58.0.3029.110 Safari/537.36'}
        html = requests.get(url)
        print(url)
        content = html.text
        print(content)
        filename = str(self.pagenumber)+".html"
        f = open(filename, 'w')
        f.write(content)
        f.close()

array = []

for i in range(2,3):
    array.append(Downloader(i))

for thread in array:
    thread.start()

for thread in array:
    thread.join()
    
    



'''
for i in range(1,101):
    url = "http://hypem.com/latest/" + str(i) + "/"
    html = urlopen(url)
    content = html.read()
    filename = str(i)+".html"
'''

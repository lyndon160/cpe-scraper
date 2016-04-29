from bs4 import BeautifulSoup
import requests

class Scrapper:

    def collectDeviceLinks(soup):
        print "Collecting"
        global devices
        group = soup.find("div", {"class": "mw-category"})
        for div in group:
            links = div.findAll('a')
            for a in links:
                    devices.append("https://wikidevi.com/w/index.php?title=Category:Wireless_embedded_system&pageuntil=AirVast+WR-2000" + a['href'])
            return




    r  = requests.get("https://wikidevi.com/w/index.php?title=Category:Wireless_embedded_system&pageuntil=AirVast+WR-2000#mw-pages", verify=False)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    global devices
    devices = []
    turnPageDiv = soup.find("div", {"id": "mw-pages"})
    collectDeviceLinks(soup)
    r  = requests.get("https://wikidevi.com/w/index.php?title=Category:Wireless_embedded_system&pageuntil=AirVast+WR-2000" + turnPageDiv.findAll('a')[0]['href'], verify=False)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    collectDeviceLinks(soup)
    turnPageDiv = soup.find("div", {"id": "mw-pages"})

    #collect device pages
    for i in range(1, 1):
        r  = requests.get("https://wikidevi.com/w/index.php?title=Category:Wireless_embedded_system&pageuntil=AirVast+WR-2000" + turnPageDiv.findAll('a')[1]['href'], verify=False)
        data = r.text
        soup = BeautifulSoup(data, 'lxml')
        collectDeviceLinks(soup)
        turnPageDiv = soup.find("div", {"id": "mw-pages"})
    	print i

    #Goto each device page and get details
    for deviceLink in devices:
        print deviceLink
        r = requests.get(deviceLink, verify=False)
        data = r.text
        soup = BeautifulSoup(data, 'lxml')
        text = soup.find("div", {"id": "mw-content-text"})
        print r.text

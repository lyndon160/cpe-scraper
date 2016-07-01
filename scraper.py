#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import time
import pickle
class Scrapper:

    def collectDeviceLinks(soup):
        print "Collecting"
        global devices
        group = soup.find("div", {"class": "mw-category"})
        for div in group:
            links = div.findAll('a')
            for a in links:
                    devices.append("https://wikidevi.com" + a['href'])
            return




    r  = requests.get("https://wikidevi.com/w/index.php?title=Category:Wireless_embedded_system&pageuntil=AirVast+WR-2000#mw-pages")
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    global devices
    devices = []
    turnPageDiv = soup.find("div", {"id": "mw-pages"})
    collectDeviceLinks(soup)
    r  = requests.get("https://wikidevi.com/w/index.php?title=Category:Wireless_embedded_system&pageuntil=AirVast+WR-2000" + turnPageDiv.findAll('a')[0]['href'])
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    collectDeviceLinks(soup)
    turnPageDiv = soup.find("div", {"id": "mw-pages"})

    #collect device pages
    for i in range(1, 19):
        r  = requests.get("https://wikidevi.com/w/index.php?title=Category:Wireless_embedded_system&pageuntil=AirVast+WR-2000" + turnPageDiv.findAll('a')[1]['href'])
        data = r.text
        soup = BeautifulSoup(data, 'lxml')
        collectDeviceLinks(soup)
        turnPageDiv = soup.find("div", {"id": "mw-pages"})
        print i

    deviceList = []

    #Goto each device page and get details
    for index, deviceLink in enumerate(devices):
        try:
            print (index)
            r = requests.get(deviceLink)
            data = r.text
            soup = BeautifulSoup(data, 'lxml')
            text = soup.find("div", {"id": "mw-content-text"})
            x = 0
            date = ""
            cpu = ""
            ram = ""
            rom = ""
            #Search through side table
            for i in text.contents[0].contents:
                #Get specs
                if("CPU" in unicode(i)):
                    for c in i.contents:
                        if("MHz" in unicode(c)):
                            cpu = unicode(c).strip('<b>').strip('</b>')
                if("FLA" in unicode(i)):
                    for c in i.contents:
                        if("MiB" in unicode(c) and not rom):
                            rom = c.contents
                        elif("MiB" in unicode(c) and not ram):
                            ram = c.contents

                #Get date
                if("FCC" in unicode(i)):
                    for d in i.contents:
                        for m in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
                            if(m in unicode(d)):
                                date = d
                if (date and cpu and rom and ram):
                    #print (unicode(date) + " CPU " + unicode(cpu) + " Flash " + unicode(rom[0].contents[0].contents[0]) + " Memory " + unicode(ram[0].contents[0].contents[0]))#.strip('<span class="smwtext">()').strip('</span>'))
                    #deviceStats = {unicode(date), unicode(cpu).strip("MHz"), unicode(rom[0].contents[0].contents[0]).strip("MiB"), unicode(ram[0].contents[0].contents[0]).strip("MiB")}
                    deviceStats = {}
                    deviceStats['URL'] = deviceLink
                    deviceStats['Date'] = unicode(date).strip()
                    deviceStats['CPU'] = unicode(cpu).strip("MHz").strip()
                    deviceStats['Flash'] = unicode(rom[0].contents[0].contents[0]).strip("MiB").strip()
                    deviceStats['Memory'] = unicode(ram[0].contents[0].contents[0]).strip("MiB").strip()
                    deviceList.append(deviceStats)
                    #print deviceStats
                    break
                x+=1
            print deviceList
            fileObject =  open('rawResults.txt', 'wb')
            pickle.dump(deviceList, fileObject)
            fileObject.close()
        except:
            print "Unexpected error"

#!/usr/bin/python
import csv
import matplotlib.pyplot as plt
import pickle
import numpy as np

from numpy import *
from matplotlib.pyplot import *
import matplotlib.patches as mpatches




devicesFile = open('Devices.csv')
devicesReader = csv.reader(devicesFile)
devicesData = list(devicesReader)

dateList = []
RAMList = []
FlashList = []
WirelessList =[]
WiredList = []

#date
for d in devicesData:

	#if not empty
	if(d[1] and d[2] and d[3] and d[4] and d[5] and "none" not in d[4] and "Release" not in d[5]):


		dateList.append(float(d[5]))
		FlashList.append(float(unicode(d[1].decode('utf-8')).split()[0].strip(','))) #need first value
		RAMList.append(float(unicode(d[2].decode('utf-8')).split()[0].strip(','))) #need first value
		lanSpeed = 0
		if("1000" in d[3]):
			lanSpeed = 1000
		elif("100" in d[3]):
			lanSpeed = 100
		else:
			lanSpeed = 10
		WiredList.append(lanSpeed) #if contains 10, 100 , 1000

		wirelessSpeed = 0
		if("ac" in d[4] and "legacy" not in d[4]):
			wirelessSpeed = 1300
		elif("n" in d[4]):
			wirelessSpeed = 450
		elif("g" in d[4]):
			wirelessSpeed = 54
		else:
			wirelessSpeed = 11

		WirelessList.append(wirelessSpeed) #if contains ac...

#average results per year
def averageResults(a , b):
    #for every duplicate a add the b equivalent
    matches = zip (a, b)
    #Find unique dates
    dates = list(set(a))
    histDict = {}
    #Collect all results with that date
    for d in dates:
        histDict[d] = 0
        count = 0
        for m in matches:
            if(m[0] == d):
                histDict[d] = histDict[d] + m[1]
                count+=1
        #Average that hist
        if(histDict[d]):
            print(d, histDict[d], count, histDict[d]/count)
            histDict[d]=histDict[d]/count
    return histDict





flashAverage = averageResults(dateList, FlashList)
print flashAverage.keys()
print flashAverage.values()
lineWeight=5
coefficients = polyfit(np.array(flashAverage.keys()), np.array(flashAverage.values()), 3)
#coefficients = polyfit(np.array(dateList), np.array(FlashList), 3)

polynomial = np.poly1d(coefficients)
#xs = np.linspace(np.amax(np.array(dateList)), np.amin(np.array(dateList)), 50, endpoint=True)
xs = np.linspace(np.amax(np.array(dateList)), np.amin(np.array(dateList)), 50, endpoint=True)
ys = polynomial(xs)
plt.plot(np.array(flashAverage.keys()), np.array(flashAverage.values()),'o', xs, ys, linewidth=lineWeight)
plt.ylabel('ROM MiB')
plt.xlabel('Years')
plt.show()



ramAverage = averageResults(dateList, RAMList)

#coefficients = polyfit(np.array(dateList), np.array(RAMList), 3)

coefficients = polyfit(np.array(ramAverage.keys()), np.array(ramAverage.values()), 3)

polynomial = np.poly1d(coefficients)
xs = np.linspace(np.amax(np.array(dateList)), np.amin(np.array(dateList)), 50)
ys = polynomial(xs)
plt.plot(np.array(ramAverage.keys()), np.array(ramAverage.values()),'o', xs, ys, linewidth=lineWeight)
plt.ylabel('RAM MiB')
plt.xlabel('Years')
plt.show()



wiredAverage = averageResults(dateList, WiredList)

#coefficients = polyfit(np.array(dateList), np.array(WiredList), 3)
coefficients = polyfit(np.array(wiredAverage.keys()), np.array(wiredAverage.values()), 3)
polynomial = np.poly1d(coefficients)
xs = np.linspace(np.amax(np.array(dateList)), np.amin(np.array(dateList)), 50)
ys = polynomial(xs)


plt.plot(np.array(wiredAverage.keys()), np.array(wiredAverage.values()), 'o', xs, ys, linewidth=lineWeight)

plt.ylabel('Mbps')
plt.xlabel('Years')
plt.show()


wirelessAverage = averageResults(dateList, WirelessList)

#coefficients = polyfit(np.array(dateList), np.array(WirelessList), 4)

coefficients = polyfit(np.array(wirelessAverage.keys()), np.array(wirelessAverage.values()), 4)
polynomial = np.poly1d(coefficients)
xs = np.linspace(np.amax(np.array(dateList)), np.amin(np.array(dateList)), 50)
ys = polynomial(xs)



plt.plot(np.array(wirelessAverage.keys()), np.array(wirelessAverage.values()), 'o', xs, ys, linewidth=lineWeight)

coefficients2 = polyfit(np.array(wiredAverage.keys()), np.array(wiredAverage.values()), 3)
polynomial2 = np.poly1d(coefficients2)
xs2 = np.linspace(np.amax(np.array(dateList)), np.amin(np.array(dateList)), 50)
ys2 = polynomial2(xs2)


plt.plot(np.array(wiredAverage.keys()), np.array(wiredAverage.values()), 'o', xs2, ys2, linewidth=lineWeight)


wired_patch = mpatches.Patch(color='c', label='Wired')
wireless_patch = mpatches.Patch(color='green', label='Wireless')
plt.legend(handles=[wired_patch, wireless_patch])



plt.ylabel('Mbps')
plt.xlabel('Years')
plt.show()






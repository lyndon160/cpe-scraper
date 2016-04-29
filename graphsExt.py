#!/usr/bin/python
import csv
import matplotlib.pyplot as plt
import pickle
import numpy as np

from numpy import *
from matplotlib.pyplot import *




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


#m, b = np.polyfit(np.array(dateList), np.array(FlashList), 1)
coefficients = polyfit(np.array(dateList), np.array(FlashList), 3)
polynomial = np.poly1d(coefficients)
xs = np.linspace(np.array(dateList)[0], np.array(dateList)[-1], 50)
ys = polynomial(xs)
plt.plot(np.array(dateList), np.array(FlashList),'o', xs, ys)
#plt.plot(np.array(dateList), m*np.array(dateList) + b, '-')
plt.ylabel('ROM MiB')
plt.xlabel('Years')
plt.show()


coefficients = polyfit(np.array(dateList), np.array(RAMList), 5)
polynomial = np.poly1d(coefficients)
xs = np.linspace(np.array(dateList)[0], np.array(dateList)[-1], 50)
ys = polynomial(xs)
plt.plot(np.array(dateList), np.array(RAMList),'o', xs, ys)
plt.ylabel('RAM MiB')
plt.xlabel('Years')
plt.show()


coefficients = polyfit(np.array(dateList), np.array(WiredList), 5)
polynomial = np.poly1d(coefficients)
xs = np.linspace(np.array(dateList)[0], np.array(dateList)[-1], 50)
ys = polynomial(xs)


plt.plot(np.array(dateList), np.array(WiredList), 'o', xs, ys)

plt.ylabel('Mbps')
plt.xlabel('Years')
plt.show()

coefficients = polyfit(np.array(dateList), np.array(WirelessList), 5)
polynomial = np.poly1d(coefficients)
xs = np.linspace(np.array(dateList)[0], np.array(dateList)[-1], 50)
ys = polynomial(xs)



plt.plot(np.array(dateList), np.array(WirelessList), 'o', xs, ys)

plt.ylabel('Mbps')
plt.xlabel('Years')
plt.show()




	

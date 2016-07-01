#!/usr/bin/python
import matplotlib.pyplot as plt
import pickle

import numpy as np

from numpy import *
from matplotlib.pyplot import *





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






fileObject = open('rawResults.txt','r')
# load the object from the file into var b
deviceList = pickle.load(fileObject)

#Get last 4 digits of date (Year)
dates = []
CPU = 	[]
ROM = 	[]
RAM = 	[]
for d in deviceList:
	dates.append(int(d.get('Date')[-4:]))
	CPU.append(int(d.get('CPU')))
	RAM.append(float(d.get('Memory').strip('MiB')))
	ROM.append(float(d.get('Flash').strip('MiB')))

print deviceList

print dates, CPU

cpuAverage = averageResults(dates, CPU)

print cpuAverage



lineWeight=5
coefficients = polyfit(np.array(cpuAverage.keys()), np.array(cpuAverage.values()), 3)

polynomial = np.poly1d(coefficients)
xs = np.linspace(2016, 1998, 50, endpoint=True)
ys = polynomial(xs)
plt.plot(np.array(cpuAverage.keys()), np.array(cpuAverage.values()),'o', xs, ys, linewidth=lineWeight)
plt.ylabel('CPU MHz')
plt.xlabel('Years')
plt.show()




plt.scatter(cpuAverage.keys(), cpuAverage.values())

plt.ylabel('CPU MHz')
plt.xlabel('Years')
plt.show()




plt.scatter(dates, CPU)

plt.ylabel('CPU MHz')
plt.xlabel('Years')
plt.show()


plt.scatter(dates, ROM)
plt.ylabel('ROM MiB')
plt.xlabel('Years')

plt.show()
plt.scatter(dates, RAM)
plt.ylabel('RAM MiB')
plt.xlabel('Years')

plt.show()

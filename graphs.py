#!/usr/bin/python
import matplotlib.pyplot as plt
import pickle

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

print dates, CPU

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

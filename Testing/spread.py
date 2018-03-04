import gspread
from oauth2client.service_account import ServiceAccountCredentials
from decimal import Decimal
import time
from time import mktime
import os
from datetime import datetime
from datetime import date
from datetime import time as datetimetime
from datetime import timedelta
from pymongo import MongoClient

"""
os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
date = time.strftime('%x')
"""

client = MongoClient('127.0.0.1')
db = client.datastore
cycleTable = db.cycleTable

hourTest = timedelta(hours = 1)
dayTest = timedelta(days = 1)
now = datetime.now()

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
masterSpreadsheet = client.open("Cycle distances")

sheet = masterSpreadsheet.worksheet("Form Responses 1")

# Extract and print all of the values
fullData = sheet.get_all_records()

distance = 0
bestDayDistance = 0
bestHourDistance = 0
lastDay = []
lastHour = []

"""
#Most recent records

for i in range(-1, -6, -1):
	print (str(fullData[i]['Please enter your name below']) +' : '+str(fullData[i]['Enter your distance below']) + 'km')
"""

print("The five most recent rides are:")

recentPlaces = 5
for i in reversed(fullData):
	distance = distance + i['Enter your distance below']

	if recentPlaces > 0:
		print (str(i['Please enter your name below']) +' : '+str(i['Enter your distance below']) + 'km')
		
	recentPlaces = recentPlaces - 1

	timeStamp = datetime.fromtimestamp(mktime(time.strptime(i['Timestamp'], "%m/%d/%Y %H:%M:%S")))
	#print (timeStamp.day)
	if now.day == timeStamp.day:
		lastDay.append(i)
		if i['Enter your distance below'] > bestDayDistance:
			bestDayDistance = i['Enter your distance below']
			bestDayRider = i['Please enter your name below']
		if now - timeStamp <= hourTest:
			lastHour.append(i)
			if i['Enter your distance below'] > bestHourDistance:
				bestHourDistance = i['Enter your distance below']
				bestHourRider = i['Please enter your name below']


print("the best ride today was by " +bestDayRider+ " with " +str(bestDayDistance)+ "km")

print("the best ride in the last hour was by " +bestHourRider+ " with " +str(bestHourDistance)+ "km")





avg = round(Decimal(distance / len(fullData)), 2)

print ("The total distance is " + str(distance))
print ("The average distance is " + str(avg))



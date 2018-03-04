from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret_LiveAccount.json', scope)

#fullData = sheet.get_all_values()
#top10Data = fullData[6:15]

#dollarMultiplier = 3

def index(request):

    client = gspread.authorize(creds)

    masterSpreadsheet = client.open("CycleForCharityResponses")
    sheet = masterSpreadsheet.worksheet("DataFormula")
    
    fullData = sheet.get_all_values()
    top10Data = fullData[6:11]
    #for value in top10Data:
    #	value.insert(1, round((float(value[1])*dollarMultiplier), 2))
    recent10 = fullData[17:27]
    if recent10[0][0]=="#VALUE!":
        backupSheet = masterSpreadsheet.worksheet("NameDistance")
        backupData = backupSheet.get_all_values()
        recent10 = backupData
    	#recent10 = []
    	#for x in range(0,10):
    	#	recent10.append(" ")
    #for value in recent10:
    #	value.insert(1, round((float(value[1])*dollarMultiplier), 2))
    #myList = [1,2,3,4,5]
    data = {'collatedValues' : fullData, 'top10' : top10Data, 'recent10' : recent10}
    return render(request, 'dashboard/index.html', data)
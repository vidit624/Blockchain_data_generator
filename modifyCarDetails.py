import requests
import datetime
import time
import random
import string
import xlrd
loc=("ChasisNumbers.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
chasisList=[]
for row in range(1,sheet.nrows):
	chasisList.append(int(sheet.cell_value(row,0)))
statuslist=["Transferred_to_Dealer","Transferred_to_Customer","NEW"]
file1 = open("modifyDetails.txt","w")
for i in range (4):
	chasisNumber= random.choice(chasisList)
	chasisNumber = str(chasisNumber)
	status=random.choice(statuslist)
	letters = string.ascii_lowercase
	dealer=''.join(random.choice(letters) for j in range(random.randint(5,15)))
	owner=''.join(random.choice(letters) for j in range(random.randint(5,15)))
	letters = string.ascii_lowercase+string.digits
	license=''.join(random.choice(letters) for j in range(7))
	L=["\nChasis Number - ",chasisNumber,"\nStatus - ",status,"\nDealer - ",dealer,"\nOwner - ",owner,"\nLicense - ",license,"\nComputer Timestamp - "]
	L="".join(str(word)for word in L)
	file1.writelines(L)
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y.%m.%d.%H.%M.%S.%f')[:-3]
	L=[st,"\n"]
	L="".join(str(word)for word in L)
	file1.writelines(L)
	url = 'http://localhost:9090/api/invoke'
	query = "{\n \"channelID\": \"cartrackingchannel\",\n \"ccId\": \"ctrack\",\n \"userId\": \"vidit\",\n \"funcName\": \"modifyCarDetails\",\n \"args\": [{\n \"chasisNumber\": \""+chasisNumber+"\",\n \"dealer\": \""+dealer+"\",\"licNumber\": \""+license+"\",\n \"status\": \""+status+"\"\n}\n],\n \"peers\": [\n\"peer0.vectorcars.com\"\n]\n}"
	res = requests.post(url, data=query)
	a=res.text.split(',')
	ts = a[len(a)-1][1:len(a[len(a)-1])-2].split(': ')
	serverTs=ts[len(ts)-1]
	L=[serverTs,"\n"]
	L="".join(str(word)for word in L)
	file1.writelines(L)
	print(res.text)
file1.close()
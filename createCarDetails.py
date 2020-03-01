import requests
import datetime
import time
import random
import string
import xlsxwriter
colorlist=["Maroon","Brown","Olive","Teal","Navy","Black","Red","Orange","Yellow","Lime","Green","Cyan","Blue","Purple","Magenta","Grey","Pink","Lavender","White"]
statuslist=["Transferred_to_Dealer","Transferred_to_Customer","NEW"]
file1 = open("createdetails.txt","w")
chasisList=[]
for i in range(4):
	chasisNumber=random.sample(range(100000,1000000),1)
	# chasisList.append(chasisNumber[0])
	chasisNumber = "".join(str(word) for word in chasisNumber)
	chasisList.append(chasisNumber)
	makeYear=random.randint(2000,2020)
	makeYear = str(makeYear)
	letters = string.ascii_lowercase
	model=''.join(random.choice(letters) for j in range(random.randint(5,15)))
	color=random.choice(colorlist)
	color = "".join(str(word) for word in color)
	L=["\nChasis Number - ",chasisNumber,"\nMake Year - ",makeYear,"\nModel - ",model,"\nColor - ",color,"\nQuery Timestamp - "]
	L = "".join(str(word) for word in L)
	file1.writelines(L)
	ts = time.time()
	url = 'http://localhost:9090/api/invoke'
	query = "{\n \"channelID\": \"cartrackingchannel\",\n \"ccId\": \"ctrack\",\n \"userId\": \"vidit\",\n \"funcName\": \"createCarDetails\",\n \"args\": [{\n \"chasisNumber\": \""+chasisNumber+"\",\n \"makeYear\": \""+makeYear+"\",\n \"model\": \""+model+"\",\n \"color\": \""+color+"\"\n}\n],\n \"peers\": [\n\"peer0.vectorcars.com\"\n]\n}"
	res = requests.post(url, data=query)
	queryTs = datetime.datetime.fromtimestamp(ts).strftime('%Y.%m.%d.%H.%M.%S.%f')[:-3]
	L=[queryTs,"\nServer Timestamp -"]
	L="".join(str(word)for word in L)
	file1.writelines(L)
	a=res.text.split(',')
	ts = a[len(a)-1][1:len(a[len(a)-1])-2].split(': ')
	serverTs=ts[len(ts)-1]
	L=[serverTs,"\n"]
	L="".join(str(word)for word in L)
	file1.writelines(L)
	print(res.text)
file1.close()
workbook = xlsxwriter.Workbook('ChasisNumbers.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
worksheet.write(0,0,"Chasis Numbers")
for data in chasisList:
	worksheet.write(row+1, col, str(data))	
	row += 1
workbook.close()
import requests
from bs4 import BeautifulSoup

print("################################")
print("Xinhua Daily. PDF download.")
print("By vvzero.com\n")

year = int(input('Please input the year: '))
month = int(input('Please input the month: '))
date = int(input('Please input the date: '))

year_str = str(year)

if month < 10 :
	month_str = '0'+str(month)
else:
	month_str = str(month)

if date < 10 :
	date_str = '0'+str(date)
else:
	date_str = str(date)

print("Downloading, please wait...")
mainpageurl = 'http://xh.xhby.net/mp3/pc/layout/'+year_str+month_str+'/'+date_str
mainpage = requests.get(mainpageurl+'/l1.html')
mainpage.encoding = 'utf-8'


mainsoup = BeautifulSoup(mainpage.text, 'html.parser')
pagelist = BeautifulSoup(str(mainsoup.find(id='layoutlist')), 'html.parser')



for pagelink in pagelist.find_all('a'):
	pageurl = 'http://xh.xhby.net/mp3/pc/layout/'+year_str+month_str+'/'+date_str+'/'+pagelink.get('href')
	page = requests.get(pageurl)
	page.encoding = 'utf-8'
	pagesoup = BeautifulSoup(page.text, 'html.parser')
	
	
	
	pdf = requests.get(mainpageurl+'/'+pagesoup.find(id='pdfUrl').string, stream=True)

	# Throw an error for bad status codes
	pdf.raise_for_status()

	with open(year_str+month_str+date_str+'-'+pagelink.get('href').split('.', 1)[0]+'.pdf', 'wb') as handle:
		for block in pdf.iter_content(1024):
			handle.write(block)

print('Done. Thank you!')
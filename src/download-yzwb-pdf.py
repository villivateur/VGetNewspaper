import requests

print("################################")
print("Yangzi evening news. PDF download.")
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


# 下载A版
count = 1
if count < 10 :
	count_str = '0'+str(count)
else:
	count_str = str(count)

pdf = requests.get('http://epaper.yzwb.net/images/'+year_str+'-'+month_str+'/'+date_str+'/A'+count_str+'/'+year_str+month_str+date_str+'A'+count_str+'_pdf.pdf', stream=True)

while pdf.status_code == 200:
	with open('yzwb'+year_str+month_str+date_str+'A'+count_str+'.pdf', 'wb') as handle:
		for block in pdf.iter_content(1024):
			handle.write(block)

	count += 1
	if count < 10 :
		count_str = '0'+str(count)
	else:
		count_str = str(count)

	pdf = requests.get('http://epaper.yzwb.net/images/'+year_str+'-'+month_str+'/'+date_str+'/A'+count_str+'/'+year_str+month_str+date_str+'A'+count_str+'_pdf.pdf', stream=True)
	

# 下载B版
count = 1
if count < 10 :
	count_str = '0'+str(count)
else:
	count_str = str(count)

pdf = requests.get('http://epaper.yzwb.net/images/'+year_str+'-'+month_str+'/'+date_str+'/B'+count_str+'/'+year_str+month_str+date_str+'B'+count_str+'_pdf.pdf', stream=True)

while pdf.status_code == 200:
	with open('yzwb'+year_str+month_str+date_str+'B'+count_str+'.pdf', 'wb') as handle:
		for block in pdf.iter_content(1024):
			handle.write(block)

	count += 1
	if count < 10 :
		count_str = '0'+str(count)
	else:
		count_str = str(count)

	pdf = requests.get('http://epaper.yzwb.net/images/'+year_str+'-'+month_str+'/'+date_str+'/B'+count_str+'/'+year_str+month_str+date_str+'B'+count_str+'_pdf.pdf', stream=True)

print('Done. Thank you!')
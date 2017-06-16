import requests, json
from bs4 import BeautifulSoup


urls = ['http://www.illinoiscourts.gov/SupremeCourt/Historical/JusticeTL.asp', 'http://www.illinoiscourts.gov/SupremeCourt/Historical/JusticeTL1a.asp','http://www.illinoiscourts.gov/SupremeCourt/Historical/JusticeTL2.asp','http://www.illinoiscourts.gov/SupremeCourt/Historical/JusticeTL3.asp']
all_supremes = {}


for url in urls:
	print(url)
	result = requests.get(url)

	if result.status_code != 200:
		print(result)
		print('Error downloading',url)
		continue

	soup = BeautifulSoup(result.content, "html.parser")

	supremes = soup.find_all("a")


	for supreme in supremes:

		# print(supreme.get('href'))

		href = supreme.get('href')
		if '../Justices/Bio_' in supreme.get('href') or '../JusticeArchive/Bio_' in supreme.get('href'):

			key = supreme.get('href').replace('../Justices/','').replace('.asp','').replace('../JusticeArchive/','')

			if key not in all_supremes:
				all_supremes[key] = {'name':'','image':'','date':'', 'start':'','end':'','url':''}
			
			image = supreme.find_all('img')

			if len(image) > 0:
				all_supremes[key]['image'] = image[0].get('src')
			else:
				all_supremes[key]['url'] = 'http://www.illinoiscourts.gov/SupremeCourt/' + href.replace('../','')

				name = supreme.text.split('\n')[0].strip()
				date = supreme.text.split('\n')[1].strip()
				start = date.split('-')[0]
				end = date.split('-')[1]

				if end == 'Present':
					end = ''
				
				all_supremes[key]['name'] = name
				all_supremes[key]['date'] = date
				all_supremes[key]['start'] = start
				all_supremes[key]['end'] = end



				# all_supremes[key]['image'] = image[0].get('src')

json.dump(all_supremes,open('scrape1.json','w'))

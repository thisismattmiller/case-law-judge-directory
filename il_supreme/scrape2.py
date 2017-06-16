import requests, json, os.path
from urllib.parse import urljoin, urlsplit
from bs4 import BeautifulSoup

data = json.load(open('scrape1.json','r'))

for judge in data:
	print(data[judge]['url'])

	if 'bio' in data[judge]:
		print('Already did it')
		continue

	result = requests.get(data[judge]['url'])


	if result.status_code != 200:
		print('Error downloading',url)
		continue

	soup = BeautifulSoup(result.content, "html.parser")

	content = soup.find("table", {'class':'content'})

	content_p = content.find_all('p')

	image_url = ''
	data[judge]['bio'] = ''

	for p in content_p:

		if p.find('img'):
			data[judge]['image'] = urljoin(data[judge]['url'],p.find('img').get('src'))
			
			image_file_name = os.path.splitext(os.path.basename(urlsplit(data[judge]['image']).path))
			data[judge]['imageLocal'] = image_file_name[0] + image_file_name[1]

			r = requests.get(data[judge]['image'])
			if r.status_code == 200:
				with open('assets/%s' % data[judge]['imageLocal'], 'wb') as f:
					f.write(r.content)

		data[judge]['bio'] = data[judge]['bio'] + p.text

	#didn't work
	if data[judge]['bio'] == '':

		content_td = content.find_all('td')

		for td in content_td:

			if td.find('img'):
				data[judge]['image'] = urljoin(data[judge]['url'],td.find('img').get('src'))
				
				image_file_name = os.path.splitext(os.path.basename(urlsplit(data[judge]['image']).path))
				data[judge]['imageLocal'] = image_file_name[0] + image_file_name[1]

				r = requests.get(data[judge]['image'])
				if r.status_code == 200:
					with open('assets/%s' % data[judge]['imageLocal'], 'wb') as f:
						f.write(r.content)

			data[judge]['bio'] = data[judge]['bio'] + td.text

	if data[judge]['bio'] == '':
		print("error on",data[judge]['url'])
		break

	json.dump(data,open('scrape2.json','w'))
		# print(p)

	# break
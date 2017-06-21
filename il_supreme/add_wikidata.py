import requests, json
# from SPARQLWrapper import SPARQLWrapper, JSON

data = json.load(open('output.json','r'))

for judge in data:
	if 'wikidata' not in data[judge]:
		print( data[judge]['wikipedia_slug'])

		#ask wikipedia about the page, and get the new slug if there is one ad the wikidata id
		result = requests.get("https://en.wikipedia.org/w/api.php?action=query&titles=%s&format=json&redirects&prop=pageprops" % data[judge]['wikipedia_slug'])

		if result.status_code != 200:
			print(result)
			print('Error downloading',url)
			continue

		result = json.loads(result.content)
		
		if 'redirects' in result['query']:
			for r in result['query']['redirects']:
				data[judge]['wikipedia_slug'] = r['to'].replace(' ','_')

		if 'pages' in result['query']:

			for page_id in result['query']['pages']:
				data[judge]['wikipedia_page_id'] = page_id
				if 'pageprops' in result['query']['pages'][page_id]:
					if 'wikibase_item' in result['query']['pages'][page_id]['pageprops']:
						data[judge]['wikidata'] = result['query']['pages'][page_id]['pageprops']['wikibase_item']
						print(data[judge]['wikidata'])

	json.dump(data,open('output.json','w'))


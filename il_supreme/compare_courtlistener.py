import json

path = '/Users/thisismattmiller/Downloads/courtlistener_judges/'
cl_judges = []

for _ in range(8519):
	data = json.load(open(path + str(_+1) + '.json','r'))

	cl_judges.append({'uri':data['resource_uri'], 'first':data['name_first'],'last':data['name_last'],'positions':data['positions'], 'date_dob': data['date_dob'], 'date_dod':data['date_dod']})

data = json.load(open('scrape2.json','r'))


for judge in data:


	for cl_judge in cl_judges:		
		if cl_judge['first'] in data[judge]['name'] and cl_judge['last'] in data[judge]['name']:

			#if we can varify by DOB that is at least in range
			if (cl_judge['date_dob']):
				cl_dob_year = int(cl_judge['date_dob'][0:4])
				year = int(data[judge]['start'])

				#were they born after our judge started?
				if cl_dob_year > year:
					continue

			if (cl_judge['date_dod']):
				cl_dod_year = int(cl_judge['date_dod'][0:4])
				year = int(data[judge]['start'])

				#did they die before they started serving?
				if year > cl_dod_year:
					continue

			# add them to the possible matches
				


			if 'possible_cl_match' not in data[judge]:
				data[judge]['possible_cl_match'] = []
			data[judge]['possible_cl_match'].append(cl_judge)



json.dump(data,open('output.json','w'))


	

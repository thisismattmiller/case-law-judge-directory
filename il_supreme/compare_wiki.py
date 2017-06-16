import json, re
wkikipedia_data = """* [[Anne M. Burke]] (2006-Present)
* [[Lloyd A. Karmeier]] (2004-Present)
* [[Rita B. Garman]] (2001-Present)
* [[Mary Jane Theis]] (2010-Present)
* [[Robert R. Thomas]] (2000-Present)
* [[Charles E. Freeman]] (1990-Present)
* [[Thomas L. Kilbride]] (2000-Present)
* [[Carroll C. Boggs]] (1897–1906)
* [[Joseph N. Carter]] (1894–1903)
* [[James H. Cartwright]] (1895–1924)
* [[Jesse J. Phillips]] (1893–1901)
* [[Joseph M. Bailey]] (1888–1895)
* [[Jacob W. Wilkin]] (1888–1907)
* [[Benjamin D. Magruder]] (1885–1906)
* [[Simeon P. Shope]] (1885–1894)
* [[Damon G. Tunnicliff]] (1885–1885)
* [[David J. Baker, Jr.]] (1888–1897)
* [[John H. Mulkey]] (1879–1888)
* [[David J. Baker, Jr.]] (1878–1879)
* [[T. Lyle Dickey]] (1875–1885)
* [[Alfred M. Craig]] (1873–1900)
* [[John Scholfield]] (1873–1893)
* [[William K. McAllister]] (1870–1875)
* [[Benjamin R. Sheldon]] (1870–1888)
* [[John M. Scott]] (1870–1888)
* [[Anthony Thornton (representative)|Anthony Thornton]] (1870–1873)
* [[Charles B. Lawrence]] (1864–1873)
* [[Corydon Beckwith]] (1864–1864)
* [[Pinkney H. Walker]] (1858–1888)
* [[Sidney Breese]] (1857–1878)
* [[Onias C. Skinner]] (1855–1858)
* [[Walter B. Scates]] (1853–1857)
* [[Lyman Trumbull]] (1848–1853)
* [[David M. Woodson]] (1848–1848)
* [[Jesse B. Thomas, Jr.]] (1847–1848)
* [[William A. Denning]] (1847–1848)
* [[Norman H. Purple]] (1845–1848)
* [[Gustavus P. Koerner]] (1845–1848)
* [[James Shields (politician, born 1810)|James Shields]] (1843–1845)
* [[Jesse B. Thomas, Jr.]] (1843–1845)
* [[John Dean Caton]] (1843–1864)
* [[John McCracken Robinson|John M. Robinson]] (1843–1843)
* [[Richard M. Young]] (1843–1847)
* [[James Semple]] (1843–1843)
* [[John D. Caton|John Dean Caton]] (1842–1843)
* [[Stephen A. Douglas]] (1841–1843)
* [[Samuel Hubbel Treat, Jr.|Samuel H. Treat]] (1841–1855)
* [[Walter B. Scates]] (1841–1847)
* [[Sidney Breese]] (1841–1843)
* [[Thomas Ford (politician)|Thomas Ford]] (1841–1842)
* [[Theophilus W. Smith]] (1825–1842)
* [[Samuel D. Lockwood]] (1825–1848)
* [[Thomas Reynolds (Governor)|Thomas Reynolds]] (1822–1825)
* [[William Wilson (Illinois jurist)|William Wilson]] (1819–1848)
* [[Joseph Phillips (jurist)|Joseph Phillips]] (1818–1822)
* [[Thomas C. Browne]] (1818–1848)
* [[William P. Foster (jurist)|William P. Foster]] (1818–1819)
* [[John Reynolds (U.S. politician)|John Reynolds]] (1818–1825)
* [[S. Louis Rathje]] (1999–2000)
* [[Michael Anthony Bilandic]] (1994–1997)
* [[Mary Ann G. McMorrow]] (1992–2006)
* [[Moses Harrison|Moses W. Harrison II]] (1992–2002)
* [[John L. Nickels]] (1992–1998)
* [[Benjamin K. Miller (judge)|Benjamin K. Miller]] (1984–2001)
* [[Joseph F. Cunningham]] (1991–1992)
* [[James D. Heiple]] (1990–2000)
* [[Horace L. Calvo]] (1988–1991)
* [[John J. Stamos]] (1988–1990)
* [[Joseph F. Cunningham]] (1987–1988)
* [[Seymour Simon]] (1980–1988)
* [[Thomas E. Kluczynski]] (1978–1980)
* [[William G. Clark]] (1976–1992)
* [[Caswell J. Crebs]] (1975–1976)
* [[Thomas J. Moran]] (1976–1992)
* [[James A. Dooley]] (1976–1978)
* [[Howard C. Ryan]] (1970–1990)
* [[Joseph H. Goldenhersh]] (1970–1987)
* [[Charles H. Davis (judge)|Charles H. Davis]] (1970–1975)
* [[Marvin Burt|Marvin F. Burt]] (1969–1970)
* [[Caswell J. Crebs]] (1969–1970)
* [[John T. Culbertson, Jr.]] (1969–1970)
* [[Thomas E. Kluczynski]] (1966–1976)
* [[Daniel P. Ward]] (1966–1990)
* [[Robert C. Underwood]] (1962–1984)
* [[Roy Solfisburg|Roy J. Solfisburg, Jr.]]  (1962–1963)
* [[Byron O. House]] (1957–1969)
* [[Charles H. Davis]] (1955–1960)
* [[Ray Klingbiel|Ray I. Klingbiel]] (1953–1969)
* [[Walter V. Schaefer]] (1951–1976)
* [[Harry B. Hershey]] (1951–1966)
* [[George W. Bristow]] (1951–1961)
* [[Ralph L. Maxwell]] (1951–1956)
* [[Albert M. Crampton]] (1948–1953)
* [[Joseph E. Daily]] (1948–1965)
* [[Jesse L. Simpson|Jessie L. Simpson]] (1947–1951)
* [[Charles H. Thompson (Illinois)|Charles H. Thompson]] (1942–1950)
* [[William J. Fulton]] (1942–1954)
* [[June C. Smith]] (1941–1947)
* [[Loren E. Murphy]] (1939–1948)
* [[Walter T. Gunn]] (1938–1951)
* [[Francis S. Wilson]] (1935–1951)
* [[Elwyn R. Shaw]] (1933–1942)
* [[Lott R. Herrick]] (1933–1937)
* [[Paul Farthing]] (1933–1942)
* [[Norman L. Jones]] (1931–1940)
* [[Warren H. Orr]] (1930–1939)
* [[Paul Samuell]] (1929–1930)
* [[Cyrus E. Dietz]] (1928–1929)
* [[Oscar E. Heard]] (1927–1928)
* [[Frank K. Dunn]] (1907–1933)
* [[Frederic R. DeYoung]] (1924–1934)
* [[Oscar E. Heard]] (1924–1933)
* [[Floyd E. Thompson]] (1919–1928)
* [[Clyde E. Stone]] (1918–1948)
* [[Warren W. Duncan]] (1915–1933)
* [[Albert Watson (Illinois judge)|Albert Watson]] (1915–1915)
* [[Charles C. Craig]] (1913–1918)
* [[George A. Cooke]] (1909–1919)
* [[Frank K. Dunn]] (1907–1933)
* [[Orrin N. Carter]] (1906–1924)
* [[Alonzo K. Vickers]] (1906–1915)
* [[William M. Farmer]] (1906–1931)
* [[Guy C. Scott]] (1903–1909)
* [[James B. Ricks]] (1901–1906)
* [[John P. Hand]] (1900–1913)
* [[Thomas R. Fitzgerald (judge)|Thomas R. Fitzgerald]] (2000–2010)
* [[Phillip J. Rarick|Philip J. Rarick]] (2002–2004)"""


wiki_data = []
for line in wkikipedia_data.split('\n'):
	if line.strip() == '':
		pass

	pat1 = re.match('\*\s\[\[(.*?)\]\]\s+\(([0-9]{4})[–|\-](.*?)\)',line,re.M|re.I)
	pat2 = re.match('\*\s\[\[(.*?)\|(.*?)\]\]\s+\(([0-9]{4})[–|\-](.*?)\)', line, re.M|re.I)

	if (pat2):
		slug = pat2.group(1)
		name = pat2.group(2)
		start = pat2.group(3)
		end =  pat2.group(4)	


	elif (pat1):
		slug = pat1.group(1)
		name = pat1.group(1)
		start = pat1.group(2)
		end =  pat1.group(3)

	else:
		print('No mattttch')
		print(line)
		break

	wiki_data.append({'name':name,'slug':slug,'start':start,'end':end})

data = json.load(open('scrape2.json','r'))

found = []
for judge in data:

	for wiki in wiki_data:
		# easy :) https://en.wikipedia.org/wiki/[slug]
		if data[judge]['name'] == wiki['name']:
			data[judge]['wikipedia_slug'] = wiki['slug'].replace(' ','_')
			data[judge]['wikipedia_name'] = wiki['name']
			found.append(wiki['name'])
	

	#didnt work, try Jr.
	if 'wikipedia_slug' not in data[judge]:
		for wiki in wiki_data:
			if data[judge]['name'] + ', Jr.' == wiki['name']:
				data[judge]['wikipedia_slug'] = wiki['slug'].replace(' ','_')
				data[judge]['wikipedia_name'] = wiki['name']
				found.append(wiki['name'])

	#didnt work, try taking out the middle inital.
	# if 'wikipedia_slug' not in data[judge]:
	# 	for wiki in wiki_data:
	# 		if re.sub('\s[A-Z].\s',' ',data[judge]['name']) == wiki['name']:
	# 			data[judge]['wikipedia_slug'] = wiki['slug'].replace(' ','_')
	# 			data[judge]['wikipedia_name'] = wiki['name']
	# 			found.append(wiki['name'])




for wiki in wiki_data:
	if wiki['name'] not in found:
		print('Could not match this wiki',wiki['name'])


for judge in data:
	if 'wikipedia_slug' not in data[judge]:
		print('Could not match this judge to wiki',judge)

json.dump(data,open('scrape2.json','w'))
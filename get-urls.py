import requests as r
with open(URLFILE) as f:
	urls = f.readlines()
params = {'username': [USERNAME], 'password': [PASS]}
token = r.post(URL, params=params)
for i in urls:
	response = r.get(i, cookies=token.cookies)
	name = urlparse.urlstip(i)[2].replace('/','-')[1:]
	f = open(name, 'w')
	f.write(response.content)
	f.close()

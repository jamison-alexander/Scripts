import requests as re
import urlparse

with open('filename') as file:
	lines = f.read().splitlines()

for f in lines:
	name = urlparse.urlparse(f).path.split('/')[-1]
	req = re.get(f, stream=True)
	with open(name, 'wb') as fd:
		for chunk in req.iter_content(chunk_size=128):
			fd.write(chunk)

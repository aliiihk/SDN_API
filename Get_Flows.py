import requests
import json

api_url_base = 'http://localhost:8080/'
flows =  'stats/flow/1'

response = requests.get(api_url_base + flows)

if response.status_code == 200:
	print json.loads(response.content.decode('utf-8'))
else:
	print "Error"

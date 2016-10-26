import urllib2
import base64
import json

def ping(site,query,key):
	
	bingUrl = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Composite?Query=%27site%3a'+ site +'%20'+ query +'%27&$top=10&$format=json'
	#Provide your account key here
	accountKey = key

	accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
	headers = {'Authorization': 'Basic ' + accountKeyEnc}
	req = urllib2.Request(bingUrl, headers = headers)
	response = urllib2.urlopen(req)
	content = response.read()
	#content contains the xml/json response from Bing. 
	cont = json.loads(content)
#	print cont['d']['results'][0]['WebTotal']
	return cont['d']['results'][0]['WebTotal']

#key = 'bing_acct_key'

#print ping('fifa.com','boardfsb',key)

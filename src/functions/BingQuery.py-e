import urllib2
import base64
import json

def ping(site,query,key):
	
	bingUrl = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Composite?Query=%27site%3a'+ site +'%20'+ query +'%27&$top=4&$format=json'
	
	#Provide your account key here
	accountKey = key
	
	top4=[]
	accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
	headers = {'Authorization': 'Basic ' + accountKeyEnc}
	req = urllib2.Request(bingUrl, headers = headers)
	response = urllib2.urlopen(req)
	content = response.read()

	#content contains the xml/json response from Bing. 
	bingweb = json.loads(content)['d']['results'][0]

	for i in bingweb['Web']:
		top4.append(str(i['Url'].encode("utf-8")))

	

	return int(bingweb['WebTotal']), top4

# key = 'WYXV0SfCQlIR7tkKc38KqcSi91X6jGGlNPCnJyZjgtg'
# count, top4 = ping('fifa.com','motherboard',key)

# print count
# print top4
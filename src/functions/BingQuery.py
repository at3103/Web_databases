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

	selected_length = 4 if int(bingweb['WebTotal']) > 4 else int(bingweb['WebTotal'])

	for i in range(selected_length):
		#print bingweb['Web'][i]['Url'].encode("utf-8")
		top4.append(str(bingweb['Web'][i]['Url'].encode("utf-8")))
	#print query,top4	
	return int(bingweb['WebTotal']), top4

# key = 'WYXV0SfCQlIR7tkKc38KqcSi91X6jGGlNPCnJyZjgtg'
# count, top4 = ping('fifa.com','motherboard',key)

# print count
# print top4

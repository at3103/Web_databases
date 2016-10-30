import urllib2
import base64
import json

def ping(site,query,key):
	
	bingUrl = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Composite?Query=%27site%3a'+ site +'%20'+ query +'%27&$top=10&$format=json'
	#Provide your account key here
	accountKey = key
	top4=[]
	accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
	headers = {'Authorization': 'Basic ' + accountKeyEnc}
	req = urllib2.Request(bingUrl, headers = headers)
	response = urllib2.urlopen(req)
	content = response.read()
	#content contains the xml/json response from Bing. 
	cont = json.loads(content)
#	print cont['d']['results'][0]['WebTotal']
	print cont['d']['results'][0]['Url']
	for i in range(4):
		top4.append(cont['d']['results'][i]['Url'])
	return cont['d']['results'][0]['WebTotal']
'''
def ping_top4(site,query,key):

	bingUrl = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Composite?Query=%27site%3a'+ site +'%20'+ query +'%27&$top=10&$format=json'
	#Provide your account key here
	accountKey = key
	top4 = []
	accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
	headers = {'Authorization': 'Basic ' + accountKeyEnc}
	req = urllib2.Request(bingUrl, headers = headers)
	response = urllib2.urlopen(req)
	content = response.read()
	#content contains the xml/json response from Bing. 
	cont = json.loads(content)
#	print cont['d']['results'][0]['WebTotal']
	print cont['d']['results'][0]['Url']
	for i in range(4):
		top4.append(cont['d']['results'][i]['Url'])
	return top4
'''
#key = '2OR+OyjGjnltNG8Nuc2Q8y2w5CYKtpgxYtem+wWzEgk'

#print ping('fifa.com','boardfsb',key)

def displayPages(label):
	print "Creating Content Summary for:" + label.name   
	count = 1
	for links in label.top4links:
		print count,"/",len(label.top4links)
		count += 1
		for page in links:
			print "Getting page: " + page 
		print " "	

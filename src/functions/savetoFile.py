from .. classes.classification import *

def savetoFile(node, content_summary,host):
	filename = node.name + "-" + host + ".txt"
	#filename = node + "-" + host + ".txt"

	f = open(filename, 'w')

	for i in range(0,len(content_summary)):
		line = str(content_summary[i][0])+"#" + str(content_summary[i][1]) + "\n"
		line = str(line)
		f.write(line)

	f.close()	

# savetoFile("root",[('the',3),('a',2)],"fifa.com")	

#$import src.queries as q
from src.functions.add_qterms import *
from src.functions.BingQuery import *
from src.glob.scheme import *
from src.algorithm.qProber import *
import sys
from src.key.key import *
from src.functions.displayPages import *
import time
import subprocess
from collections import Counter

# tec = 12000
# tes = 0.02
Add_qterms()

for di in d.keys():
	toptemp = []
	for query in d[di].q_terms:
		#print di,query
		count, top4 = ping('fifa.com',query,key)
		#time.sleep(5)
		temp = []
		for link in top4:
			if link not in toptemp:
				toptemp.append(link)
				temp.append(link)
		#d[di].parent.topSet += temp		
		d[di].parent.top4links.append(temp)
		d[di].assign_coverage(float(count))
		# d[di].parent.top4links.append(top4)
		# d[di].assign_coverage(float(count))
	d[di].parent.topSet.update(toptemp) 		
assign_lvl_coverage()
		
for di in d.keys():
	d[di].compute_specificity()

#for di in d.keys():
#	print di + "Coverage ",d[di].cov
#	print di + "Specificity",d[di].spec

#print "root : ", root.total_cov
#display(root)
for child in root.child:
	display(child)
#	classify(child,tec,tes)
	classify(child)	
print " "
for w in label_list:
	print w	
#classify (root,tec,tes)



print "Extracting topic content summaries..."
#displayPages(root)
displaylist =[]
displaylist.append(root)

for child in root.child:
	if any(child.name in string for string in label_list): 
		for qlinks in child.top4links:
			temp = []
			for links in qlinks:
				if links not in root.topSet:
					root.topSet.update(links)
					temp.append(links)
			root.top4links.append(temp)#child.top4links 
		displaylist.append(child)

for node in displaylist:
	displayPages(node)

#getWordsLynx(root)		

#For every link in label.topSet call java file using subprocess. Append returned strings to a list

subprocess.call(["javac", "src/getWordsLynx.java"])

for node in displaylist:
	words = []
	for link in node.topSet:
		words += subprocess.call(["java","src/getWordsLynx", link]).strip().split()
	node.cont_sum_list += words
	count_set = Counter(node.cont_sum_list)
	print "Contet summary for " + node.name
	print count_set






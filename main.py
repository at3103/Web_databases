from src.functions.check_sanity import *
from src.functions.add_qterms import *
from src.functions.BingQuery import *
from src.glob.scheme import *
import sys
from src.key.key import *
from src.functions.displayPages import *
import time
import subprocess
from collections import Counter
from time import sleep
from src.algorithm.qProber import *
from src.functions.savetoFile import *
import operator
from src.functions.savetoFile import *

# Host Database
host = sys.argv[3]

# Fetching and saving query terms from txt files
Add_qterms()

# Bing Query with corresponding host and query to get top 4 links for each query (Generating document samples) 
for di in d.keys():
	toptemp = []
	for query in d[di].q_terms:
		count, top4 = ping(host,query,key)
		temp = []
		for link in top4:
			if link not in toptemp:
				toptemp.append(link)
				temp.append(link)
		d[di].parent.top4links.append(temp)
		# Computing coverage
		d[di].assign_coverage(float(count))
	d[di].parent.topSet.update(toptemp) 		

# Computing specificity
assign_lvl_coverage()		
for di in d.keys():
	d[di].compute_specificity()

# Classifying the host database
print "CLASSIFICATION\n"
for child in root.child:
	display(child)
	classify(child)	
	
print " "
for w in label_list:
	print w	
print " " 

# Appending to Root document samples its children's document samples if classified so
print "\nExtracting topic content summaries..."
displaylist =[]
displaylist.append(root)
ll = list(root.topSet)

for child in root.child:
	if any(child.name in string for string in label_list): 
		for qlinks in child.top4links:
			temp = []
			for links in qlinks:
				if links not in root.topSet:
					ll.append(links)
					temp.append(links)
			root.top4links.append(temp) 
		displaylist.append(child)

# Printing the document samples
for node in displaylist:
	displayPages(node)
root.topSet = set(ll)

#Generating Content Summaries
s = subprocess.Popen(["javac", "src/getWordsLynx.java"], stderr= subprocess.PIPE)
for node in displaylist:
	words = []
	for link in node.topSet:
		# Ignoring PDFs and PPTs
		if link.endswith(".pdf") or link.endswith(".ppt"): 
			continue
		else:
			proc = subprocess.Popen(["java","getWordsLynx", link], stdout=subprocess.PIPE, cwd =r'src')
			st = proc.communicate()[0]
			doc_words = set(st.strip().strip('\x00').split())
			words+=list(doc_words)
	# Generating document Frequency for each category		
	count_set = Counter(words)
	sorted_count_set = sorted(count_set.items(), key=operator.itemgetter(0))
	# Saving the Content Summary to file
	savetoFile(node,sorted_count_set,host)




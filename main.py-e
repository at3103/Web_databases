#$import src.queries as q
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

if len(sys.argv) != 4:
	print "Wrong format: Provide arguments in this parameter <t_es> <t_ec> <host>"
	sys.exit()

if(float(sys.argv[1]) > 1 or float(sys.argv[1]) < 0):
	print "Specificity threshold should be 0 - 1"
	sys.exit()

if(float(sys.argv[2]) < 1):
	print "Invalid value for t_c"
	sys.exit()


#Threshold must be btw 0 and 1 else break
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

print "CLASSIFICATION\n"

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

print root.topSet
print " " 


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
					print links +'\n'
					ll.append(links)
					temp.append(links)
			root.top4links.append(temp) 
		displaylist.append(child)

for node in displaylist:
	displayPages(node)

root.topSet = set(ll)

#For every link in label.topSet call java file using subprocess. Append returned strings to a list
s = subprocess.Popen(["javac", "src/getWordsLynx.java"], stderr= subprocess.PIPE)

for node in displaylist:
	words = []
	for link in node.topSet:
		print link
		if link.endswith(".pdf") or link.endswith(".ppt"):
			continue
		else:
		#if "pdf" not in link or "ppt" not in link: #Ignoring PDFs and PPTs
			subprocess.call(["cd","src"])
			proc = subprocess.Popen(["java","getWordsLynx", link], stdout=subprocess.PIPE, cwd =r'src')
			st = proc.communicate()[0]
			words += st.strip().strip('\x00').split()

	node.cont_sum_list += words
	count_set = Counter(node.cont_sum_list)
	print "Content summary for " + node.name
	print count_set





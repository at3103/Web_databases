#$import src.queries as q
from src.functions.add_qterms import *
from src.functions.BingQuery import *
from src.glob.scheme import *
from src.algorithm.qProber import *
import sys
from src.key.key import *
from src.functions.displayPages import *
import time

# tec = 12000
# tes = 0.02
Add_qterms()

for di in d.keys():
	for query in d[di].q_terms:
		print di,query
		count, top4 = ping('fifa.com',query,key)
		#time.sleep(5)
		d[di].parent.top4links.append(top4)
		d[di].assign_coverage(float(count))
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
displayPages(root)

for child in root.child:
	if any(child.name in string for string in label_list): 
		displayPages(child)






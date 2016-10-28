#$import src.queries as q
from src.functions.add_qterms import *
from src.functions.BingQuery import *
from src.glob.scheme import *
from src.algorithm.qProber import *
import sys



key = 'bing_acct_key'
tec = 12000
tes = 0.7
Add_qterms()

for di in d.keys():
	for query in d[di].q_terms:
		count = ping('fifa.com',query,key)
		 #d[di].cov+=int(count)
		d[di].assign_coverage(float(count))
for di in d.keys():
	d[di].compute_specificity()

#for di in d.keys():
#	print di + "Coverage ",d[di].cov
#	print di + "Specificity",d[di].spec

#print "root : ", root.total_cov
#display(root)
for child in root.child:
	display(child)
	classify(root.name,child,tec,tes)
print " "
print classification	
#classify (root,tec,tes)


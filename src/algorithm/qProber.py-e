from src.functions.add_qterms import *
from src.glob.scheme import *

classification = []
base = root.name
count = 0 

def classify(base,label,tec,tes):
	if label.cov > tec and label.spec > tes:
		base = base, "/", label.name
		for child in label.child:
			display(child)
			classify(base,child,tec,tes)
			base = root.name
		classification.append(base)		 
		
	'''	
	for child in label.child:
		#count += 1
		if child.cov>tec and child.spec>tes:
			storeClass(child)
			classify(child,tec,tes)
		#if count == child.ch_count:
	'''	

				

def display(label):
	print "Specificity for category:"+label.name+ " is ",label.spec			
	print "Coverage for category:"+label.name+ " is ",label.cov		

def storeClass(label):
	c = label.name+"/"



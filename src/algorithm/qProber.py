from src.functions.add_qterms import *
from src.glob.scheme import *
from src.classes.given import *

classification = []
count = 0 

#tec = 12000
#tes = 0.02
th = threshold(70000, 0.0001)

#Check Threshold!!!!
tec = th.tec
tes = th.tes

# def classify(label,tec,tes):
def classify(label):
	if label.cov >= tec and label.spec >= tes:
		if label.ch_count <= 0:
			classification.append(label.path)			
			label.parent.flag = 3
		else:
			for child in label.child:
				display(child)
				classify(child)

	elif  label.parent.flag != 3:
		if label.parent.flag != label.parent.ch_count-1:
			label.parent.flag += 1
		else:
			classification.append(label.parent.path)		

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



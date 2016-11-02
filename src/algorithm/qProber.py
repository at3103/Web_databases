from src.functions.add_qterms import *
from src.glob.scheme import *
from src.classes.given import *

label_list = []
count = 0 

#Check Threshold!!!!
tec = th.tec
tes = th.tes

# def classify(label,tec,tes):
def classify(label):
	if label.cov >= tec and label.spec >= tes:
		if label.ch_count <= 0:
			label_list.append(label.path)			
			label.parent.flag = 3
		else:
			for child in label.child:
				display(child)
				classify(child)

	elif  label.parent.flag != 3:
		if label.parent.flag != label.parent.ch_count-1:
			label.parent.flag += 1
		else:
			label_list.append(label.parent.path)		

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



from .. classes.classification import *
from .. glob.scheme import *



def Add_qterms():
	
	filenames = ['root', 'sports', 'health', 'computers']

	for name in filenames:
		f = open('src/queries/'+ name + '.txt','r')
		word_list = []
		for line in f:
			l = line.strip()
			line_words = l.split()
			obj = line_words[0]

			word_list = l[len(obj)+1:]
			word_list = word_list.replace(" ","%20")
			d[obj].q_terms.append(word_list)
			
	# for di in d.keys():
	# 	print di + " : " ,d[di].q_terms
	# for c in range(root.ch_count):
	# 	print root.child[c]

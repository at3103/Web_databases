
class Label(object):
	lvl_list = []

	"""docstring for Label"""
	def __init__(self, name,cov,spec):
		super(Label, self).__init__()
		self.name = name
		self.cov = cov
		self.spec = spec
		self.parent = []
		self.child = []
		self.ch_count = 0
		self.q_terms = []
		self.total_cov = 0
		self.path = 'Root'
		self.level = 0
		self.flag = 0
		self.top4links = []
		self.topSet = set()
		self.cont_summary = []

	def link_parent(self,parent):
		self.parent = parent
		self.path = parent.path + '/' + self.name 
		parent.link_child(self)
		self.assign_level()

	def link_child(self,child):
		self.child.append(child)
		self.ch_count +=1		

	def assign_coverage(self, cov):
		self.cov += cov
		self.parent.total_cov += cov

	def assign_level(self):
		self.level = self.parent.level + 1	

	def assign_lvl_coverage(object):

		lvl_list[0] = 0 
		lvl_list[1] = root.total_cov
		lvl_list[2] = 0
		for child in root.child:
			lvl_list[2] += child.total_cov

	def compute_specificity(self):
		self.spec = self.cov/Label.lvl_list[self.level]

	def display(self):
		print "P1:" + self.name 
		print self.ch_count
		count = self.ch_count - 1
		while(count >= 0):
			print "C" , self.ch_count - count , " : " , self.child[count].name
			count -= 1



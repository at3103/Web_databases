class Label(object):
	"""docstring for Label"""
	def __init__(self, name,cov,spec):
		super(Label, self).__init__()
		self.name = name
		self.cov = cov
		self.spec = spec
		self.parent = []
		self.child = []
		self.ch_count = 0
		self.q_terms =[]
		self.total_cov = 0


	def link_parent(self,parent):
		self.parent = parent
		parent.link_child(self)

	def link_child(self,child):
		self.child.append(child)
		self.ch_count +=1		

	def assign_coverage(self, cov):
		self.cov += cov
		self.parent.total_cov += cov

	def compute_specificity(self):
		self.spec = self.cov/self.parent.total_cov

	def display(self):
		# temp = Label("temp", 0, 0)
		# temp = self
		# while(temp.)
		print("P1:" + self.name )
		count = self.ch_count - 1 
		while(count >= 0):
			print("C" , self.ch_count - count , " : " + self.child[count].name)
			count -= 1


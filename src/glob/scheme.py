from .. classes.classification import *

root = Label("Root", 0, 0)
computers = Label("Computers", 0, 0)
health = Label("Health", 0, 0)
sports = Label("Sports", 0, 0)
basketball = Label("Basketball", 0, 0)
soccer = Label("Soccer", 0, 0)
fitness = Label("Fitness", 0, 0)
diseases = Label("Diseases", 0, 0)
hardware = Label("Hardware", 0, 0)
programming = Label("Programming", 0, 0)

sports.link_parent(root)
health.link_parent(root)
computers.link_parent(root)
programming.link_parent(computers)
hardware.link_parent(computers)
diseases.link_parent(health)
fitness.link_parent(health)
soccer.link_parent(sports)
basketball.link_parent(sports)

computers.display()
root.display()
d = { "Programming" : programming,
		"Hardware"	: hardware,
		"Diseases"	: diseases,
		"Fitness"	: fitness,
		"Basketball": basketball,
		"Soccer"	: soccer,
		"Sports"	: sports,
		"Health"	: health,
		"Computers"	: computers,
}

def assign_lvl_coverage():

	Label.lvl_list.append(0) 
	Label.lvl_list.append(root.total_cov)
	Label.lvl_list.append(0) 
	for child in root.child:
		Label.lvl_list[2] += child.total_cov
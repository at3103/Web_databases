import sys

if len(sys.argv) != 4:
	print "Wrong format: Provide arguments in this parameter <t_es> <t_ec> <host>"
	sys.exit()

if(float(sys.argv[1]) > 1 or float(sys.argv[1]) < 0):
	print "Specificity threshold should be 0 - 1"
	sys.exit()

if(float(sys.argv[2]) < 1):
	print "Invalid value for t_c"
	sys.exit()

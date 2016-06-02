import sys
import fileinput
for line in fileinput.input(sys.argv[2]):
	print line,
#print sys.argv[1].split(',')


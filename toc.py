import sys
import fileinput

c = 0

pair = sys.argv[1].split(',')
for line in fileinput.input(sys.argv[2]):
	print line,
	for ppp in pair:
		x=ppp.split('#')
		if (x[0] in line) and (x[1]in line):
			c=c+1
print c

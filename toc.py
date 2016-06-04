import sys
import fileinput

c=0
result = []
pair = sys.argv[1].split(',')
for ppp in pair:
	result.append(0)
	c=c+1
total_pair=c
for line in fileinput.input(sys.argv[2]):
	index=0
	for ppp in pair:
		x=ppp.split('#')
		if (x[0] in line) and (x[1]in line):
			result[index]=result[index]+1
		index=index+1

for x in range(total_pair):
	print result[x]

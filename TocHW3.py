#-*- coding: utf-8 -*-
#學號:F74026331
#姓名:吳念祖
#描述:我利用python內建的函式去處理字串，例如:in & split。也利用dict這個型別來處理結果，因此可以直接用sort來排序。整體來說就是利用pythonuf強大的字串處理功能來寫程式碼。
import sys
import fileinput
result = []
pair = sys.argv[1].split(',')
for ppp in pair:
	result.append(0)
for line in fileinput.input(sys.argv[2]):
	index=0
	for ppp in pair:
		x=ppp.split('#')
		title = line.split("\t")
		if (x[0] in title[0]) and (x[1]in title[0]):
			result[index]=result[index]+1
		index=index+1
final = dict(zip(pair,result))
for x, y in sorted(final.iteritems(), key=lambda(key,value): (value,key), reverse=True):
	print "%s,%s" % (x, y) 

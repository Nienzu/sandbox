#-*- coding: utf-8 -*-
#學號:F74026331
#姓名:吳念祖
#描述:我利用python內建的函式去處理字串，例如:in & split。也利用dict這個型別來處理結果，因此可以直接用sort來排序。整體來說就是利用pythonuf強大的字串處理功能來寫程式碼。這次作業跟hw3要注意的是換行會包進去split出來後的string, 所以要特別做處理。除此之外，我這次的作業跟hw3老實說我覺得差異不大，頂多只有一些判斷式的改。
import sys
import fileinput
ex = dict()
for line in fileinput.input(sys.argv[2]):
	title = line.split("\t")
	title[2] = title[2].rstrip('\n')
	if (title[0] == title[2]):
		if(not ex.has_key(title[0])):
			ex[title[0]]=2
		else:
			ex[title[0]]= ex[title[0]]+2
	else:
		if ex.has_key(title[0]) and ex.has_key(title[2]):
			ex[title[0]]= ex[title[0]]+1
			ex[title[2]]= ex[title[2]]+1
		elif not ex.has_key(title[0]) and ex.has_key(title[2]):
			ex[title[0]]=1
			ex[title[2]]=ex[title[2]]+1
		elif ex.has_key(title[0]) and not ex.has_key(title[2]):
			ex[title[0]]=ex[title[0]]+1
			ex[title[2]]=1
		else:
			ex[title[0]]=1
			ex[title[2]]=1
k=int(sys.argv[1])
degree = -1
for x, y in sorted(ex.iteritems(), key=lambda(key,value): (value,key), reverse=True):	
	if degree != y:	
		degree = y
		k=k-1
	if k < 0:
		break
	print "%s,%s" % (x.rstrip('\n'), y) 
		

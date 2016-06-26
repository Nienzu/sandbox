# -*- coding:utf-8 -*-
#F74021103 資訊三甲 郭珮羽 計理HW4
#input:python TocHW4.py k /home/toc/redirects_zh.csv
#output:Print keyword and the degree of the keyword sorted by the count of news in the descending order, and set the delimiter as a comma.
#description:
#每次讀一行資料，先將兩個node分別切下來放入node[]陣列中，(2*linenum)紀錄node個數
#先將node[0]放入紀錄不重複名字的name[]陣列中，計算每個名字出現的次數(=邊數)放入陣列num[]中
#再比對每個名字若出現第一次，則填入name[]陣列中，若已出現過，則次數(=邊數)加1
#最後將num[]的資料作降冪排列放入陣列finalsort[]中，將num[]中的數值依照finalsort[]中的順序，與name[]一起印出。
#遇到次數(=邊數)相同者，則依陣列checkornot[]判斷是否已經印過了。
########################################################################################################################
import sys
#import time

#start=time.time()
node=[]
name=[]
num=[]
linenum=0
namenum=1

finalsort=[]
checkornot=[]

#file = open(sys.argv[2],'r',encoding = 'utf8') #python3 method
#file = open(sys.argv[2],'r')
#content=file.readlines()
#for line in content:
for line in open(sys.argv[2],'r'):
	line=line.strip('\n')
		linenum=linenum+1
		node.append(line.split('\t')[0])
		node.append(line.split('\t')[2])

name.append(node[0])
num.append(1)

for item1 in range(1,2*linenum,1):
	flag=0
	for item2 in range(0,namenum,1):
		if node[item1] == name[item2]:
			num[item2]=num[item2]+1
			flag=1
	if flag==0:
		name.append(node[item1])
		num.append(1)
		namenum=namenum+1

for item5 in range(0,namenum,1):
	checkornot.append(0)

finalsort=sorted(num,reverse=True)
for item3 in range(0,int(sys.argv[1]),1):
	for item4 in range(0,namenum,1):
		if finalsort[item3]==num[item4] and checkornot[item4]==0:
			print(name[item4]+','+str(num[item4]))
			checkornot[item4]=1

#file.close()
#end=time.time()
#print(end-start)
